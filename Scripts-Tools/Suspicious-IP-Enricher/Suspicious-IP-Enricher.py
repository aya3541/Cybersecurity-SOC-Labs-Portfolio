
# 🌐 Suspicious IP Enricher (Threat Intel)

**Suspicious-IP-Enricher** is a SOC utility designed to automate the enrichment of IP addresses with geographic and organizational data. This helps analysts quickly identify the source of suspicious traffic and determine if an IP belongs to a known hosting provider, VPN, or proxy.

---

## 🎯 SOC Use Case
When an analyst identifies a suspicious IP in a SIEM alert or web log, they need context:
- Is this a residential IP or a Data Center?
- Is the IP coming from a country we don't do business with?
- Is it a known Proxy/VPN used to hide attacker identity?

---

## 🔍 Key Features
- **Geo-IP Mapping:** Country, City, and Timezone detection.
- **Organization Intelligence:** Identifies ISP, ASN, and Hosting providers.
- **Risk Assessment:** Flagging IPs associated with Proxies or Hosting services.
- **Automated Reporting:** Clean, SOC-style CLI output with timestamps.

---

## 🛠️ Technical Details
- **Language:** Python 3.x
- **API Used:** IP-API (JSON)
- **Libraries:** `requests`, `sys`, `datetime`

---

## 🚀 How to Run
1. Ensure the `requests` library is installed:
```bash
pip install requests

```

2. Run the script with an IP address:

```bash
python3 Suspicious_IP_Enricher.py 8.8.8.8

```

---

## 📤 Example Output

```text
============================================================
🛡️  IP THREAT INTELLIGENCE REPORT
Report Generated: 2024-05-20 15:45:10
============================================================
IP Address      : 8.8.8.8
Country         : United States
City            : Mountain View
ISP             : Google LLC
Organization    : Google LLC
ASN             : AS15169 Google LLC
Timezone        : America/Los_Angeles
------------------------------------------------------------
✅ Risk Assessment: No obvious threat indicators detected
============================================================

```

---

## 🎯 Why This Script Matters

* **Threat Intelligence Enrichment:** Demonstrates how to integrate external APIs into defensive workflows.
* **Decision Support:** Provides immediate context for better incident triage.
* **Scalability:** The clean structure (`main()` function) allows for easy integration into SOAR or SIEM tools.

---

[⬅️ Back to Scripts & Tools](./README.md)



```
