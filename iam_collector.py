import boto3
import json
import datetime
import os

# Initialize AWS IAM client
iam_client = boto3.client('iam')

def get_roles():
    """Fetch all IAM roles."""
    roles = []
    paginator = iam_client.get_paginator('list_roles')
    for page in paginator.paginate():
        roles.extend(page['Roles'])
    return roles

def get_role_policies(role_name):
    """Get inline and attached policies for a given role."""
    policies = {
        "inline_policies": {},
        "attached_policies": []
    }
    # Inline policies
    inline_policy_names = iam_client.list_role_policies(RoleName=role_name)['PolicyNames']
    for policy_name in inline_policy_names:
        policy_doc = iam_client.get_role_policy(RoleName=role_name, PolicyName=policy_name)['PolicyDocument']
        policies['inline_policies'][policy_name] = policy_doc

    # Attached managed policies
    attached_policies = iam_client.list_attached_role_policies(RoleName=role_name)['AttachedPolicies']
    for policy in attached_policies:
        policies['attached_policies'].append({
            'PolicyName': policy['PolicyName'],
            'PolicyArn': policy['PolicyArn']
        })
    return policies

def collect_iam_snapshot():
    """Collect all roles and their policies, return as dict."""
    snapshot = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "roles": []
    }
    roles = get_roles()
    for role in roles:
        role_entry = {
            "RoleName": role['RoleName'],
            "RoleId": role['RoleId'],
            "Arn": role['Arn'],
            "CreateDate": role['CreateDate'].isoformat(),
            "AssumeRolePolicyDocument": role['AssumeRolePolicyDocument'],
            "Policies": get_role_policies(role['RoleName'])
        }
        snapshot['roles'].append(role_entry)
    return snapshot

def save_snapshot(snapshot, output_dir='snapshots'):
    """Save snapshot JSON file with timestamped filename."""
    os.makedirs(output_dir, exist_ok=True)
    filename = f"iam_snapshot_{datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.json"
    path = os.path.join(output_dir, filename)
    with open(path, 'w') as f:
        json.dump(snapshot, f, indent=4)
    print(f"Snapshot saved to {path}")

def main():
    print("Starting IAM snapshot collection...")
    snapshot = collect_iam_snapshot()
    save_snapshot(snapshot)
    print("Done.")

if __name__ == "__main__":
    main()
