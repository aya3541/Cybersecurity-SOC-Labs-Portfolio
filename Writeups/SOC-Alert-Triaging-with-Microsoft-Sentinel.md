
# Case Study: Investigating Linux Privilege Escalation via Microsoft Sentinel

## 1. Executive Summary

This report details the systematic investigation of high-severity incidents detected within the Azure environment of 'The Best Festival Company'. The investigation focused on identifying a series of malicious activities involving unauthorized kernel module insertion and privilege escalation through improper sudoers modifications.

* **Attack Vector:** Unauthorized SSH access followed by exploitation of local configuration weaknesses.
* **Impact:** Root-level compromise allowing persistent access and sensitive data exfiltration (Credential Harvesting).

---

## 2. Incident Context

* **Platform:** Microsoft Sentinel (SIEM/SOAR)
* **Incident Name:** `Linux PrivEsc - Kernel Module Insertion`
* **Affected Asset:** `app-02` (Linux Web Server)
* **Verdict:** **True Positive (TP)**

**Tactics (MITRE ATT&CK):**

| Tactic | Technique |
| --- | --- |
| **Initial Access** | Valid Accounts (T1078) |
| **Privilege Escalation** | Exploitation for Privilege Escalation (T1068) |
| **Persistence** | Kernel Modules and Extensions (T1547.006) |

---

## 3. Attack Timeline (Reconstructed)

| Time (UTC) | Action |
| --- | --- |
| **10:02** | Successful SSH login from unauthorized external IP (`10.10.155.20`) |
| **10:04** | Unauthorized `sudoers` modification detected |
| **10:06** | Access to sensitive file backup (`/etc/shadow`) - Credential Harvesting |
| **10:09** | Insertion of malicious kernel module (`malicious_mod.ko`) |

---

## 4. Technical Investigation & Log Analysis

### Phase 1: Evidence Collection via KQL

A deep-dive analysis was conducted using KQL on the `Syslog_CL` table to validate the suspicious activity on the affected host.

**KQL Query Executed:**

```kusto
Syslog_CL
| where host_s == 'app-02'
| project _timestamp_t, host_s, Message
| order by _timestamp_t asc

```

### Phase 2: False Positive (FP) Consideration

Before final escalation, a rigorous False Positive review was conducted:

1. **Maintenance Window:** No approved maintenance or updates were scheduled for this period.
2. **Entity Verification:** The source IP (`10.10.155.20`) was confirmed to be outside the authorized administrative range.
3. **Command Intent:** The combination of `shadow` file access and `kernel module` insertion is inconsistent with standard administrative workflows.

---

## 5. Analysis and Impact

* **Attack Chain:** The attacker bypassed initial controls to obtain root-level access, followed by establishing persistence through a malicious kernel module to survive reboots.
* **Impact:** **High** — Full compromise of the host and potential lateral movement to other cloud assets.

**CIA Impact:**

| Property | Impact |
| --- | --- |
| **Confidentiality** | **High** - Sensitive credential hashes (`/etc/shadow`) were accessed |
| **Integrity** | **High** - Unauthorized system configuration and kernel-level changes |
| **Availability** | **Medium** - Risk of system instability due to unauthorized kernel modules |

---

## 6. Mitigation & Strategic Recommendations

### Immediate Response (SOAR Concept)

* **Host Isolation:** Automatically isolated `app-02` from the network to prevent lateral movement.
* **Identity Cleanup:** Revoked active sessions and removed the unauthorized user `Alice`.
* **Artifact Removal:** Purged `malicious_mod.ko` and restored original `sudoers` configuration.

### Long-term Hardening

* **Detection Logic:** Deploy Sentinel Analytic Rules specifically for "Kernel Module Insertion" and "Unauthorized Sudoers modification".
* **Zero Trust:** Enforce phishing-resistant MFA (FIDO2) and Just-In-Time (JIT) access for all SSH management.
* **Immutable Logs:** Ensure logs are forwarded to a hardened, central repository to prevent attacker tampering.

---

[⬅️ Back to Writeups](./README.md)

