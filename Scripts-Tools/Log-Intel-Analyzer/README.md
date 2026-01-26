
# 🔍 Log-Intel-Analyzer

## Overview
Log-Intel-Analyzer is a lightweight SOC automation script designed to identify high-frequency IP activity within web server access logs.

It supports initial incident triage by quickly highlighting IP addresses that may be associated with brute-force attacks, scanning activity, or abuse.

---

## 🛠 Use Case (SOC Perspective)
This tool is typically used during:
* **Initial alert investigation** (e.g., High traffic alerts).
* **Web server compromise triage.**
* **Suspicious traffic analysis** to find top talkers.

---

## ✨ Features
* **IPv4 extraction** using Regex.
* **Request frequency analysis.**
* **Configurable detection threshold.**
* **Clean and readable output.**

---

## 📋 Requirements
* Python 3.x
* Access log file (Apache / Nginx)

---

## 🚀 How to Run
```bash
python3 Log-Intel-Analyzer.py

```

## 📤 Example Output

```text
IP: 192.168.1.45    | Requests: 154
IP: 10.10.10.23     | Requests: 97

```

---

## 🛡 Defensive Value

This script demonstrates:

* **Log analysis fundamentals:** Transforming raw data into actionable intel.
* **Automation mindset:** Speeding up manual triage tasks.
* **SOC-level threat detection logic:** Focusing on indicators of attack (IOAs).

---

