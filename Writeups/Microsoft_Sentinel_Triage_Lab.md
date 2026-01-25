Case Study: Investigating Linux Privilege Escalation via Microsoft Sentinel

# 1. Executive Summary
This report details the systematic investigation of high-severity incidents detected within the Azure environment of 'The Best Festival Company'. The investigation focused on identifying a series of malicious activities mapped to the Privilege Escalation tactic, 
specifically involving unauthorized kernel module insertion and privilege escalation through improper sudoers modifications.

# 2. Incident Context
Platform: Microsoft Sentinel (SIEM/SOAR)

Incident Name: Linux PrivEsc - Kernel Module Insertion

Tactics (MITRE ATT&CK): Initial Access (T1078), Privilege Escalation (T1068), Persistence (T1547.006)

# 3. Attack Timeline (Reconstructed)
To demonstrate the progression of the breach, the following timeline was reconstructed from logs:

10:02 UTC: Successful SSH login from unauthorized external IP (10.10.155.20).

10:04 UTC: Privilege escalation activity detected (unauthorized sudoers modification).

10:06 UTC: Execution of sensitive file backup (/etc/shadow) indicating credential harvesting.

10:09 UTC: Deployment and insertion of malicious kernel module (malicious_mod.ko).

# 4. Technical Investigation & Log Analysis
Phase 1: Evidence Collection via KQL
A deep-dive analysis was conducted using KQL on the Syslog_CL table to validate the suspicious activity on app-02.

## KQL Query Executed:
Syslog_CL
| where host_s == 'app-02'
| project _timestamp_t, host_s, Message
| order by _timestamp_t asc
Phase 2: False Positive (FP) Consideration
Before escalation, a False Positive review was conducted:

Maintenance Window: No approved maintenance or updates were scheduled for this period.

Entity Verification: The source IP (10.10.155.20) does not belong to any authorized administrative range.

Verdict: Confirmed True Positive (TP) based on the sequence of unauthorized system-level changes.

# 5. Analysis and Impact
The attacker successfully bypassed initial controls to obtain root-level access. Impact: Full compromise of the host allowed the attacker to survive reboots (Persistence) and potentially pivot to other cloud assets or exfiltrate sensitive credential hashes from the shadow file.

# 6. Mitigation and Strategic Recommendations
Immediate Response & SOAR Concept
Host Isolation: Isolated app-02 from the network to prevent lateral movement.

Identity Cleanup: Revoked active sessions and removed the unauthorized user 'Alice'.

Artifact Removal: Purged the malicious_mod.ko from the file system.

Long-term Hardening & Detection Logic
Detection Logic: Implement alerts specifically for "Kernel Module Insertion" and "Unauthorized Sudoers modification" using Sentinel Analytic Rules.

Zero Trust: Enforce Phishing-resistant MFA (FIDO2) and Just-In-Time (JIT) access for all SSH management.

Assumptions & Limitations: Investigation relied on Sentinel-ingested Syslog data; packet-level evidence was not available during this phase.

Back to Main Writeups
