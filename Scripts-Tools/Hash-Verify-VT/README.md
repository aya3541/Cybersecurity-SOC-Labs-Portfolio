
# 🔐 Hash-Verify-VT (VirusTotal Automation)

**Hash-Verify-VT** is a Python-based SOC utility designed to automate **file hash reputation analysis** using the VirusTotal API.

The project is built with a **versioned approach**, demonstrating progressive development from basic malware triage to more advanced SOC automation capabilities.

---

## 🎯 SOC Use Case

During incident response and threat hunting, SOC analysts frequently work with:
- File hashes from EDR / XDR alerts
- Suspicious attachments from phishing campaigns
- Indicators of Compromise (IOCs) from SIEM platforms and threat intelligence feeds

Hash-Verify-VT automates the **first-stage malware triage**, significantly reducing manual lookup time and improving analyst efficiency.

---

## 📦 Project Structure & Versions

### 🧪 Version 1.0 — Core Hash Triage
📁 `v1.0/`

A lightweight script focused on **single-hash analysis**.

**Key Capabilities:**
- Supports MD5, SHA1, and SHA256 hashes
- Queries VirusTotal Public API
- Extracts malicious, suspicious, and undetected counts
- Clear verdict output for fast decision-making

📄 Documentation:  
➡️ `v1.0/README.md`

---

### 🚀 Version 2.0 — Enhanced SOC Automation
📁 `v2.0/`

An improved version designed to reflect **real SOC workflows** and analyst needs.

**Key Enhancements:**
- Batch hash scanning from input files
- CSV / JSON report generation
- Improved output formatting for case documentation
- Basic handling of VirusTotal API rate limits
- More structured and extensible codebase

📄 Documentation:  
➡️ `v2.0/README.md`

---

## 🛠️ Technical Stack

- **Language:** Python 3.x
- **Core Libraries:** `requests`, `json`, `sys`
- **External Service:** VirusTotal Public API
- **Platform:** SOC / Blue Team automation

---

## 🧠 SOC Analyst Notes

> This tool is designed for **initial malware triage**, not final verdicts.
> Results should always be correlated with:
> - Endpoint behavior (EDR telemetry)
> - Network traffic (PCAP, NetFlow)
> - Sandbox or dynamic malware analysis

---

## 🧩 Why This Project Matters

This project demonstrates:
- SOC analyst mindset
- Automation-first approach
- Understanding of malware triage workflows
- Progressive skill development through versioning
- Clean documentation and maintainable structure

---

## 🔄 Future Roadmap

- Threat scoring and confidence calculation
- SIEM integration (Sentinel / Splunk)
- IOC enrichment (GeoIP, ASN, reputation feeds)
- Automated alert generation

---


[⬅️ Back to Scripts & Tools](../README.md)

