
# 🔐 Hash-Verify-VT v1.0 (VirusTotal Automation)

**Hash-Verify-VT v1.0** is a lightweight Python script designed to help SOC analysts perform **quick malware hash reputation checks** using the VirusTotal API.

This initial version focuses on **single-hash analysis**, making it ideal for fast triage during incident response and alert investigation.

---

## 🎯 SOC Use Case

During SOC operations, analysts frequently encounter:
- File hashes extracted from EDR or antivirus alerts
- Hashes from suspicious email attachments
- Indicators of Compromise (IOCs) from threat intelligence feeds

Version 1.0 automates the **manual VirusTotal lookup process**, saving time during early-stage malware analysis.

---

## 🔍 Key Features

- Supports **MD5**, **SHA1**, and **SHA256** hashes
- Queries VirusTotal using the public API
- Extracts:
  - Malicious detection count
  - Suspicious detection count
  - Undetected engines
- Clear verdict logic (Malicious / Suspicious / Clean)
- Simple, readable terminal output

---

## 🛠️ Technical Details

- **Language:** Python 3.x
- **Libraries Used:** `requests`, `json`, `sys`
- **External Service:** VirusTotal Public API
- **Input:** Single file hash via command-line argument

---

## 📖 How to Use

### 1️⃣ Set Your API Key

Edit the script and insert your VirusTotal API key:

```python
API_KEY = "YOUR_API_KEY_HERE"
````

---

### 2️⃣ Run the Script

```bash
python3 hash_verify_vt.py <file_hash>
```

---

## 📤 Example Output

```text
========================================
🔍 VirusTotal Hash Analysis Result
========================================
Hash Type     : SHA256
Malicious     : 12
Suspicious    : 3
Undetected    : 55
Total Engines : 70
----------------------------------------
🚨 Verdict    : MALICIOUS
========================================
```

---

## ⚠️ Limitations (v1.0)

* Single hash analysis only
* No batch processing
* No report export
* Limited handling of API rate limits

These limitations are addressed in **Version 2.0**.

---

## 🧠 SOC Analyst Notes

> This script is designed for **initial malware triage**.
> Results should always be correlated with:
>
> * Endpoint behavior
> * Network activity
> * Sandbox analysis

---

## 🔄 Version Roadmap

* ✅ **v1.0:** Single hash triage
* 🚀 **v2.0:** Batch scanning + CSV reporting
* 🔜 **v3.0:** SIEM integration and IOC enrichment

---
