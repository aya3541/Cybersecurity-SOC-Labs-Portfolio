
# ⚙️ Scripts & Security Automation

This directory contains custom-built scripts and security automation utilities designed to support **SOC operations**, **log analysis**, and **incident response** workflows.

The goal of these tools is to reduce manual effort, speed up investigations, and demonstrate hands-on defensive security skills.

---

## 🚀 Featured Tool: Log-Intel-Analyzer (Python)

**Log-Intel-Analyzer** is a lightweight Python utility built for SOC analysts to quickly parse and analyze web server access logs (Apache / Nginx).

### 🔍 Key Features
- **Automated IP Extraction:** Uses Regular Expressions (Regex) to extract all IPv4 addresses from raw log files.
- **Frequency Analysis:** Identifies top-talking IP addresses using statistical counting.
- **Threat Detection Support:** Helps detect potential:
  - Brute Force attempts  
  - DDoS activity  
  - Automated directory or endpoint scanning
- **SOC Efficiency:** Reduces initial log triage time from minutes to seconds.

### 🛠️ Technical Details
- **Language:** Python 3.x
- **Libraries Used:** `re`, `collections`
- **Input:** `.log` or `.txt` web access log files

### 📖 How to Use
1. Ensure Python 3 is installed.
2. Place your log file (e.g., `access.log`) in the same directory as the script.
3. Run the script:
   ```bash
   python3 Log-Intel-Analyzer.py
````

### 📤 Example Output

```text
Top Suspicious IPs:
192.168.1.45  ->  154 requests
10.10.10.23   ->  97 requests
45.33.21.10   ->  82 requests
```

---

## 🧩 Additional SOC Automation Scripts (Planned & In Progress)

These tools are designed to reflect **real SOC analyst tasks** and defensive security workflows.

* [ ] **Hash-Verify-VT.py**
  *Automates file hash reputation checks using VirusTotal API.*
  **Focus:** Malware triage, threat intelligence enrichment.

* [ ] **Suspicious-IP-Enricher.py**
  *Enriches IP addresses with GeoIP, ASN, and threat reputation data.*
  **Focus:** Incident context, threat hunting.

* [ ] **Windows-Event-Log-Hunter.py**
  *Parses Windows Event Logs to detect suspicious login patterns and privilege escalation attempts.*
  **Focus:** Blue Team, Windows security monitoring.

* [ ] **SSH-Bruteforce-Detector.py**
  *Detects repeated failed SSH login attempts from auth.log files.*
  **Focus:** Linux security, brute-force detection.

* [ ] **Mini-SIEM-Parser.py**
  *Correlates logs from multiple sources (web + auth logs) to simulate basic SIEM logic.*
  **Focus:** Log correlation, SOC fundamentals.

---

## 🎯 Why These Scripts Matter

Each script in this directory demonstrates:

* Practical SOC analyst thinking
* Automation mindset
* Understanding of real attack patterns
* Blue Team & defensive security focus

These tools are intentionally **small, readable, and realistic**, similar to scripts used internally by SOC teams.

---

[⬅ Back to Main Portfolio](../README.md)




