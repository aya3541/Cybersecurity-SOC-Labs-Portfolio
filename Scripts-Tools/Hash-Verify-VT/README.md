
# 🔐 Hash-Verify-VT (VirusTotal Automation)

**Hash-Verify-VT** is a Python-based SOC utility that automates file hash reputation checks using the VirusTotal API.

This script helps analysts quickly determine whether a file hash is associated with known malware, significantly reducing manual lookup time during incident response and threat triage.

---

## 🎯 SOC Use Case

During malware investigations, SOC analysts often receive:
- **File hashes** from EDR or XDR alerts
- **Suspicious attachments** extracted from phishing emails
- **Indicators of Compromise (IOCs)** from SIEM platforms or threat intelligence feeds

This tool automates the **first-stage malware triage** process and supports faster decision-making.

---

## 🔍 Key Features
- **Multi-Format Hash Support:** MD5, SHA1, and SHA256
- **Automated Reputation Lookup:** Queries the VirusTotal API directly
- **Threat Intelligence Extraction:** Retrieves malicious, suspicious, and undetected detection counts
- **SOC-Friendly Output:** Clean and readable output suitable for incident documentation

---

## 🛠️ Technical Details
- **Language:** Python 3.x
- **Libraries Used:** `requests`, `json`, `sys`
- **External Service:** VirusTotal Public API
- **Input:** Single file hash (passed as a CLI argument)

---

## 📖 How to Use

1. Obtain a **VirusTotal API key**.
2. Insert your API key into the script:
```python
API_KEY = "YOUR_API_KEY_HERE"
````

3. Run the script from the terminal:

```bash
python3 hash_verify_vt.py <file_hash>
```

---

## 📤 Example Output

```text
========================================
🔍 VirusTotal Hash Analysis Result
========================================
Hash Type        : SHA256
Malicious        : 12
Suspicious       : 3
Undetected       : 55
Total Engines    : 70
----------------------------------------
🚨 Verdict: MALICIOUS
========================================
```

---

## 🧠 SOC Analyst Notes

> **Note:** This script is intended for **initial triage only**, not final verdicts.
> Results should always be correlated with:
>
> * Endpoint behavior (EDR telemetry)
> * Network activity (PCAPs, NetFlow)
> * Sandbox or dynamic analysis results

---

## 🚧 Planned Enhancements

* [ ] Batch hash scanning from input files
* [ ] CSV / JSON report export
* [ ] Public API rate-limit handling
* [ ] Threat score calculation

---
[⬅️ Back to Scripts & Tools](../README.md)

