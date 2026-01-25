
# Case Study: Windows Registry Forensics on Compromised Asset (dispatch-srv01)

## 1. Executive Summary

This report documents a forensic investigation of the Windows Registry from the host **dispatch-srv01**. The objective was to identify artifacts of a recent compromise by King Malhare's bandits. The analysis focused on identifying installed malicious software, execution paths, and persistence mechanisms.

* **Attack Vector:** Likely originated via social engineering or direct download of malicious binaries.
* **Impact:** Full system compromise allowing potential lateral movement and unauthorized access to sensitive data stored on the host.

---

## 2. Investigation Context

* **Asset Name:** `dispatch-srv01`
* **Incident Date:** October 21, 2025
* **Artifacts Analyzed:** `SYSTEM`, `SOFTWARE`, and `NTUSER.DAT` Registry Hives
* **Tools Used:** Registry Explorer (Zimmerman Tools)

---

## 3. Forensic Methodology

The investigation followed a standard forensic workflow:

* **Hive Loading:** Offline analysis of registry hives to prevent data alteration.
* **Transaction Log Replay:** Handling "dirty" hives by replaying transaction logs for data consistency.
* **Artifact Analysis:** Utilizing bookmarks and manual navigation to examine keys related to persistence and execution.
* **Assumptions & Limitations:** Investigation relied on offline registry data; packet-level evidence (PCAP) was not available for this host.

---

## 4. Attack Timeline (Reconstructed)

| Time (UTC) | Action |
| --- | --- |
| **09:15** | `Gift_Dispenser.exe` downloaded to Downloads folder |
| **09:30** | Executed via **UserAssist** tracked GUI launch |
| **09:35** | **Run Key** modified for persistence (`Malhare_Updater`) |
| **09:40** | Malicious activity established root-level foothold on the host |

---

## 5. Technical Findings

### 5.1. Software Installation & Initial Artifacts

* **Registry Key:** `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`
* **Evidence:** An application named `Gift_Dispenser.exe` was installed shortly before suspicious activity.

### 5.2. Execution Analysis

* **Registry Key:** `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist`
* **Execution Path:** `C:\Users\Administrator\Downloads\Gift_Dispenser.exe`
* **Observation:** UserAssist tracking confirmed GUI-based execution of the malicious binary.

### 5.3. Persistence Mechanism

* **Registry Key:** `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
* **Value Added:** `Malhare_Updater` pointing to the malicious executable.
* **Implication:** Ensures the binary executes automatically on user login, enabling long-term persistence.

---

## 6. False Positive Consideration

Before concluding, a review confirmed this was not a false positive:

1. **Maintenance Window:** No approved system maintenance during this period.
2. **Entity Verification:** The binary and Run key modification were unauthorized and not associated with any administrative activity.

* **Verdict:** **Confirmed True Positive (TP)** based on unauthorized system-level changes.

---

## 7. Analysis & Impact

* **Attack Chain:** The attacker successfully bypassed initial controls to gain a foothold via a direct download, followed by securing persistence through Registry modification.
* **Impact:** **High** — Full host compromise, persistent malicious access, and potential lateral movement to other assets.

| Property | Impact |
| --- | --- |
| **Confidentiality** | High risk of unauthorized access to sensitive data on `dispatch-srv01` |
| **Integrity** | Registry and system settings were modified to facilitate persistence |
| **Availability** | System remained available, but under unauthorized control |

---

## 8. Recommendations & Remediation

### Immediate Response

* **Host Isolation:** Isolate `dispatch-srv01` for full disk imaging and deeper analysis.
* **Persistence Removal:** Delete `Malhare_Updater` registry entry and the associated binary.
* **Credential Rotation:** Rotate all administrative passwords used on the host.

### Long-term Hardening

* **Registry Monitoring:** Implement EDR/SIEM alerts for unauthorized changes to `Run` and `RunOnce` keys.
* **SOAR/Automation:** Configure automated playbooks to isolate assets when registry anomalies are detected.
* **Zero Trust:** Enforce phishing-resistant MFA (FIDO2) and Just-In-Time (JIT) access for administrative accounts.

---

[⬅️ Back to Writeups](./README.md)

