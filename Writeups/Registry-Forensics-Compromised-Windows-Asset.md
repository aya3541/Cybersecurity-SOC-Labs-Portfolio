### Case Study: Windows Registry Forensics on Compromised Asset (dispatch-srv01)

## 1. Executive Summary

This report documents a forensic investigation of the Windows Registry from the host dispatch-srv01. The objective was to identify artifacts of a recent compromise by King Malhare's bandits. The analysis focused on identifying installed malicious software, execution paths, and persistence mechanisms.

Attack Vector: The compromise likely originated via social engineering or direct download of malicious binaries.
Impact: Full system compromise allowing potential lateral movement and unauthorized access to sensitive data stored on the host.

## 2. Investigation Context

Asset Name: dispatch-srv01

Incident Date: October 21, 2025

Artifacts Analyzed: SYSTEM, SOFTWARE, and NTUSER.DAT Registry Hives

Tools Used: Registry Explorer (Zimmerman Tools)

## 3. Forensic Methodology

The investigation followed a standard forensic workflow:

Hive Loading: Offline analysis of registry hives to prevent data alteration.

Transaction Log Replay: Handling "dirty" hives by replaying transaction logs for data consistency.

Artifact Analysis: Utilizing bookmarks and manual navigation to examine keys related to persistence and execution.

Assumptions & Limitations: Investigation relied on Sentinel-ingested Syslog and offline registry data; packet-level evidence was not available.

## 4. Attack Timeline (Reconstructed)

To demonstrate the progression of the compromise, the following timeline was reconstructed from registry artifacts:

Oct 21, 2025, 09:15: Gift_Dispenser.exe downloaded to Downloads folder.

Oct 21, 2025, 09:30: Executed via UserAssist tracked GUI launch.

Oct 21, 2025, 09:35: Run key modified for persistence (Malhare_Updater).

Oct 21, 2025, 09:40: Malicious activity established root-level foothold on the host.

## 5. Technical Findings
   
# 5.1. Software Installation & Initial Artifacts

Registry Key: HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall

Evidence: An application named Gift_Dispenser.exe was installed shortly before suspicious activity.

# 5.2. Execution Analysis

Registry Key: HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist

Execution Path: C:\Users\Administrator\Downloads\Gift_Dispenser.exe

Observation: UserAssist tracking confirmed GUI-based execution of the malicious binary.

# 5.3. Persistence Mechanism

Registry Key: HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

Value Added: Malhare_Updater pointing to the malicious executable.

Implication: Ensures the binary executes automatically on user login, enabling long-term persistence.

## 6. False Positive Consideration

Before concluding, a review confirmed this was not a false positive:

Maintenance Window: No approved system maintenance during this period.

Entity Verification: The binary and Run key modification were unauthorized and not associated with administrative activity.

Verdict: Confirmed True Positive (TP) based on system-level changes.

## 7. Analysis & Impact

The attacker successfully bypassed initial controls to gain a foothold.

Impact: Full host compromise, persistent malicious access, and potential lateral movement to other assets.

Attack Method: Exploitation through social engineering or direct download, followed by persistence via Run key modification.

## 8. Recommendations & Remediation

Immediate Response

Host Isolation: Isolate dispatch-srv01 for full disk imaging.

Persistence Removal: Delete Malhare_Updater registry entry and associated binary.

Credential Rotation: Rotate all administrative passwords used on the host.

Long-term Hardening & Detection Logic

Registry Monitoring: Implement EDR/SIEM alerts for unauthorized changes to Run and RunOnce keys.

SOAR/Automation: Configure automated alerts or Playbooks to isolate assets when registry anomalies are detected.

Zero Trust: Enforce Phishing-resistant MFA (FIDO2) and Just-In-Time (JIT) access for administrative accounts.

Back to Main Writeups
