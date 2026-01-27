
# 🌐 Suspicious IP Enricher (Threat Intelligence Automation)

**Suspicious-IP-Enricher** is a lightweight SOC utility that automates the enrichment of IP addresses with geographic and organizational intelligence.  
It helps SOC analysts quickly understand the context behind suspicious IP activity during investigations.

---

## 🎯 SOC Use Case
During SOC operations, analysts often encounter suspicious IP addresses from:
- SIEM alerts
- Web server logs
- Firewall or IDS events
- Brute-force or scanning activity

This script provides immediate answers to questions like:
- Where is this IP located?
- Is it coming from a hosting provider or ISP?
- Could it be a VPN, proxy, or attacker infrastructure?

---

## 🔍 Key Features
- **Geo-IP Intelligence:** Country, City, and Timezone detection.
- **Network Attribution:** ISP, Organization, and ASN information.
- **Risk Awareness:** Highlights IPs associated with hosting or proxy services.
- **SOC-Friendly Output:** Clean CLI report with timestamped results for incident tickets.

---

## 🛠️ Technical Details
- **Language:** Python 3.x
- **API Used:** IP-API (public JSON endpoint)
- **Libraries:** `requests`, `sys`, `datetime`

---

## 🚀 How to Run

### 1️⃣ Install Requirements
```bash
pip install requests

```

### 2️⃣ Run the Script

```bash
python3 Suspicious_IP_Enricher.py <IP_ADDRESS>

```

*Example:* `python3 Suspicious_IP_Enricher.py 8.8.8.8`

---

## 📤 Example Output

```text
============================================================
🛡️ IP THREAT INTELLIGENCE REPORT
Report Generated: 2024-05-20 15:45:10
============================================================
IP Address   : 8.8.8.8
Country      : United States
City         : Mountain View
ISP          : Google LLC
Organization : Google LLC
ASN          : AS15169 Google LLC
Timezone     : America/Los_Angeles
------------------------------------------------------------
✅ Risk Assessment: No obvious threat indicators detected
============================================================

```

---

## 🧠 SOC Analyst Notes

This script is designed for initial enrichment and triage only. Final decisions should always be correlated with:

* SIEM timelines.
* Firewall and IDS logs.
* Endpoint telemetry (EDR/XDR).

---

## 🚧 Planned Enhancements

* [ ] Batch IP enrichment from file.
* [ ] CSV / JSON report export.
* [ ] Integration with SIEM / SOAR workflows.

---

[⬅️ Back to Scripts & Tools](../README.md)

