إليكِ النسخة المعدلة بالكامل مع إصلاح تنسيق الأكواد (Backticks) لضمان ظهورها بشكل مثالي على GitHub، مع إضافة لمسات تنظيمية بسيطة تجعل التقرير يبدو أكثر احترافية:

---

# Case Study: Web Attack Forensics via Splunk (Drone Alone)

## 1. Executive Summary

This report documents the forensic investigation of a **Command Injection** attack targeting the TBFC drone scheduler web UI. Using **Splunk SIEM**, a multi-layered analysis was performed correlating Apache web logs with Windows Sysmon telemetry to:

* Identify the attack vector
* Decode obfuscated payloads
* Assess host-level impact

**Attack Vector:** Exploitation of a vulnerable CGI script (`hello.bat`) allowing arbitrary PowerShell command execution.

**Impact:** Remote Code Execution (RCE) enabling potential reconnaissance and unauthorized system access.

---

## 2. Investigation Context

* **Platform:** Splunk Enterprise
* **Affected Service:** Apache Web Server (Windows-based)
* **Vulnerable Component:** `/cgi-bin/hello.bat` (CGI Script)
* **Attack Type:** Command Injection (OWASP Top 10)

**Tactics (MITRE ATT&CK):**

| Tactic | Technique |
| --- | --- |
| Initial Access | Exploit Public-Facing Application (T1190) |
| Execution | Command and Scripting Interpreter (T1059) |

---

## 3. Technical Investigation & SPL Queries

### Phase 1: Web Layer Triage

The investigation began by searching `windows_apache_access` logs for command execution attempts in URI queries.

**SPL Query Executed:**

```spl
index=windows_apache_access (cmd.exe OR powershell OR "Invoke-Expression") 
| table _time, host, clientip, uri_path, uri_query, status

```

**Findings:**

* Multiple requests to `hello.bat` contained Base64-encoded PowerShell strings.
* **Payload Decoded:** `VABoAGkAcwAgAGkAcwAgAG4AbwB3ACAATQBpAG4AZQAh...`
* **Decoded Message:** `"This is now Mine! MUAAHAAHAAHAA"`

### Phase 2: Host-Level Correlation (Sysmon)

To confirm OS-level execution, process creation events were analyzed where the parent process was Apache (`httpd.exe`).

**SPL Query Executed:**

```spl
index=windows_sysmon ParentImage="*httpd.exe"
| table _time, Image, ParentImage, CommandLine

```

**Critical Finding:**

* **Confirmed `httpd.exe` spawned `cmd.exe**`
* This is a definitive indicator of successful Command Injection, as a web server should not normally spawn system shells.

### Phase 3: Post-Exploitation Reconnaissance

Common reconnaissance commands were analyzed to assess privilege context.

**SPL Query Executed:**

```spl
index=windows_sysmon *cmd.exe* *whoami*

```

**Result:**

* The attacker executed `whoami` via the injected shell to verify current user context.

---

## 4. Attack Timeline (Reconstructed)

| Time (UTC) | Action |
| --- | --- |
| 10:02 | Attempted command injection via `/cgi-bin/hello.bat` |
| 10:03 | Base64 payload detected and decoded |
| 10:04 | `httpd.exe` spawned `cmd.exe` (**RCE achieved**) |
| 10:05 | Executed `whoami` for privilege verification |

---

## 5. Analysis and Impact

* **Attack Chain:** Exploitation of a vulnerable CGI script (`hello.bat`) allowed PowerShell command execution.
* **Impact:** **High** — Remote Code Execution (RCE) achieved. Some advanced commands were blocked or failed.
* **Verdict:** True Positive (TP)

**CIA Impact:**

| Property | Impact |
| --- | --- |
| **Confidentiality** | Potential unauthorized access to sensitive information |
| **Integrity** | Risk of system manipulation via executed commands |
| **Availability** | Limited risk; core services not disrupted but could be targeted in future attacks |

---

## 6. Mitigation & Strategic Recommendations

### Immediate Response

* **Service Patching:** Disable or secure the vulnerable `hello.bat` CGI script.
* **IP Blocking:** Blacklist identified client IP at the network firewall.
* **Session Termination:** Kill all `cmd.exe` or `powershell.exe` processes spawned by `httpd.exe`.

### Long-term Hardening

* **Splunk Alerting:** Permanent alerts for any child process of `httpd.exe` spawning shells.
* **Input Validation:** Strict input sanitization on all web forms and URI parameters.
* **Least Privilege:** Ensure the web server service account has minimal permissions.
* **Zero Trust MFA:** Consider MFA for web admin access and monitoring of privileged operations.

---

[Back to Main Writeups](https://www.google.com/search?q=../Writeups/README.md)
