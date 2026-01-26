
# ⚙️ Scripts & Security Automation

This directory contains custom-built scripts and security automation utilities designed to support **SOC operations**, **log analysis**, and **incident response** workflows.

The goal of these tools is to reduce manual effort, speed up investigations, and demonstrate hands-on defensive security skills.

---

## 🚀 Featured Tool: Log-Intel-Analyzer (Python)

**Log-Intel-Analyzer** is a lightweight Python utility built for SOC analysts to quickly parse and analyze web server access logs (Apache / Nginx).

### 🔍 Key Features
- **Professional IP Extraction:** Uses advanced Regular Expressions (Regex) to accurately identify valid IPv4 addresses.
- **Frequency Analysis:** Automatically counts and sorts IP activity.
- **Alert Thresholding:** Focuses only on high-volume IPs (default: 50+ requests) to reduce noise.
- **Incident Documentation:** Generates time-stamped reports suitable for SOC case notes and forensic records.

### 🛠️ Technical Details
- **Language:** Python 3.x
- **Libraries Used:** `re`, `collections`, `datetime`
- **Input:** `.log` or `.txt` web access log files

### 📖 How to Use
1. Ensure Python 3 is installed.
2. Place your log file (e.g., `access.log`) in the same directory as the script.
3. Run the script:
```bash
python3 log_intel_analyzer.py
````

### 📤 Example Output

```text
==================================================
🛡️  SOC LOG ANALYSIS REPORT
Generated on: 2024-05-20 14:30:15
==================================================
Total Requests Analyzed : 1240
Unique IPs Detected     : 45
Alert Threshold         : 50+ requests
--------------------------------------------------
🚨 High-Frequency IPs (Potentially Suspicious):
IP: 192.168.1.45    | Requests: 154
IP: 45.33.21.10     | Requests: 82
==================================================
```

---

## 🧩 Additional SOC Automation Scripts (Planned & In Progress)

These tools reflect **real SOC analyst responsibilities** and defensive security workflows.

* [ ] **Hash-Verify-VT.py**
  *Focus: Malware triage, file reputation analysis, threat intelligence enrichment.*

* [ ] **Suspicious-IP-Enricher.py**
  *Focus: IP reputation checks, GeoIP & ASN enrichment, incident context.*

* [ ] **Windows-Event-Log-Hunter.py**
  *Focus: Windows Security Events, suspicious logins, privilege escalation detection.*

* [ ] **SSH-Bruteforce-Detector.py**
  *Focus: Linux auth.log analysis, brute-force detection.*

* [ ] **Mini-SIEM-Parser.py**
  *Focus: Log correlation, SOC fundamentals, multi-source detection logic.*

---

## 🎯 Why These Scripts Matter

Each script demonstrates:

* Practical **SOC analyst thinking**
* An **automation-first mindset**
* Understanding of real-world attack patterns (Brute Force, DDoS, Recon)
* Strong **Blue Team & defensive security focus**

These tools are intentionally **small, readable, and realistic**, similar to scripts used internally by SOC teams for daily investigations.

---

[⬅️ Back to Main Portfolio](../README.md)

