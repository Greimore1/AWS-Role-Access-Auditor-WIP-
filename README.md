# AccessAuditor

## Overview
AccessAuditor is a comprehensive tool to audit AWS IAM roles and policies to enforce least privilege principles. It automates data collection, analysis, alerting, and provides a dashboard to improve cloud security posture.

---

## Planned Phases

### Phase 1: AWS IAM Data Collector (Here now)
- Fetch all IAM roles and their inline/attached policies.
- Save snapshots locally for reference and auditing.
- Command-line interface for manual or scheduled runs.

### Phase 2: Policy Analysis Engine
- Analyse IAM policies for over-permission, wildcards, unused permissions.
- Generate actionable reports with improvement suggestions.

### Phase 3: Alerting Module
- Integrate Slack and Email notifications for alerts.
- Customisable thresholds and alert frequency.

### Phase 4: Persistent Historical Storage & API (Ambitious)
- Store snapshots and analysis results in a database.
- Build REST API for external access and dashboard consumption.

### Phase 5: Interactive Dashboard UI (Ambitious)
- Web interface to visualise roles, permissions, and suggestions.
- Role-based access control and authentication.

### Phase 6: Suggestion Engine & Advanced Analytics (Ambitious)
- Add heuristic and machine learning-based insights.
- Prioritise risky roles and permissions automatically.

### Phase 7: Deployment & CI/CD Pipeline
- Containerise application components.
- Setup automated build, testing, and deployment pipelines.

### Phase 8: Security Hardening & Documentation (Ambitious)
- Secure credential management.
- Full documentation and test coverage.




**Proof of concept project, so as not to exceed AWS free tier limits**
