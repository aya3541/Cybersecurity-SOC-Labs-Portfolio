تمام 
# 🔐 Hash-Verify-VT v2.0 (VirusTotal Automation)

**Hash-Verify-VT v2.0** is an enhanced SOC automation script that performs **advanced malware hash triage** using the VirusTotal API.

This version builds on the core functionality of v1.0 by adding **batch scanning**, **structured reporting**, and **SOC-ready output**, making it suitable for real-world incident response workflows.

---

## 🎯 SOC Use Case

During security investigations, SOC analysts frequently receive multiple file hashes from:
- EDR alerts
- Phishing investigations
- Threat intelligence feeds
- Incident response cases

Version 2.0 automates **bulk hash analysis** and produces structured results that can be directly attached to incident tickets or reports.

---

## 🚀 What's New in Version 2.0

### ✅ Enhancements Over v1.0
- **Batch Hash Scanning:** Analyze multiple hashes from a `.txt` file.
- **Structured Output:** Clear verdict per hash (Malicious / Suspicious / Clean).
- **Rate-Limit Awareness:** Handles VirusTotal public API limitations.
- **SOC-Friendly Reporting:** Outputs results in both terminal view and CSV report.

---

## 🔍 Key Features

- Supports **MD5**, **SHA1**, and **SHA256**
- Automated VirusTotal API querying
- Extracts:
  - Malicious detections
  - Suspicious detections
  - Undetected engines
- Generates a **CSV report** for documentation
- Clean, readable, analyst-friendly output

---

## 🛠️ Technical Details

- **Language:** Python 3.x
- **Libraries Used:** `requests`, `json`, `csv`, `sys`, `time`
- **External Service:** VirusTotal Public API
- **Input:** Text file containing hashes (one hash per line)

---

## 📖 How to Use

### 1️⃣ Set Your API Key
Edit the script and add your VirusTotal API key:

```python
API_KEY = "YOUR_API_KEY_HERE"
````

---

### 2️⃣ Prepare Hash List

Create a file called `hashes.txt`:

```text
44d88612fea8a8f36de82e1278abb02f
275a021bbfb648b3c0b63d50d8f6a8e9
```

---

### 3️⃣ Run the Script

```bash
python3 hash_verify_vt_v2.py hashes.txt
```

---

## 📤 Example Output (Terminal)

```text
========================================
🔍 VirusTotal Batch Hash Analysis
========================================
Hash: 44d88612fea8a8f36de82e1278abb02f
Malicious : 15
Suspicious: 2
Verdict   : MALICIOUS
----------------------------------------
Hash: 275a021bbfb648b3c0b63d50d8f6a8e9
Malicious : 0
Suspicious: 0
Verdict   : CLEAN
========================================
📄 Report saved as: vt_analysis_report.csv
```

---

## 📁 Output Files

* **vt_analysis_report.csv**

  * Hash
  * Malicious Count
  * Suspicious Count
  * Undetected Count
  * Final Verdict

---

## 🧠 SOC Analyst Notes

> This script is intended for **initial malware triage**.
> Final decisions should be correlated with:
>
> * Endpoint telemetry (EDR)
> * Network indicators
> * Sandbox execution results

---

## 🚧 Planned Enhancements (Future Versions)

* [ ] JSON export support
* [ ] VirusTotal Private API support
* [ ] Automatic IOC extraction
* [ ] SIEM integration (Splunk / Sentinel)

---


