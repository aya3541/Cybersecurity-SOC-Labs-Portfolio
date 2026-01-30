# 🔍 Case Study: Network Threat Hunting & C2 Detection (AsyncRAT Analysis)

## 1. Executive Summary
This report documents a technical threat hunting investigation focused on identifying **Command and Control (C2)** communication within network traffic. Using **RITA (Real Intelligence Threat Analytics)** and **Zeek logs**, I analyzed the `AsyncRAT.pcap` dataset to detect beaconing patterns and unauthorized connections.

* **Objective:** Identify compromised internal hosts communicating with external C2 servers.
* **Key Finding:** Detected suspicious beaconing activity from host **10.3.14.101** to multiple external IPs.
* **Attack Vector:** Automated beaconing patterns typical of **AsyncRAT** malware.
* **Impact:** Potential unauthorized system control and persistence within the network.

---

## 2. Investigation Context
* **Asset Analyzed:** Internal Segment (Subnet 10.3.14.0/24)
* **Tools Used:** * `Zeek`: For generating structured network connection logs.
    * `RITA`: For statistical analysis and beaconing detection.
    * `Linux CLI`: For manual log inspection and parsing.
* **Artifacts:** `AsyncRAT.pcap`, Zeek logs (`conn.log`, `http.log`).

---

## 3. Technical Investigation & Methodology

### Phase 1: PCAP to Zeek Conversion
The raw PCAP was processed into structured Zeek logs to enable deep flow analysis.
![Zeek Log Generation](zeek_conversion.png)
*Execution of Zeek to parse AsyncRAT.pcap and generate metadata logs.*

### Phase 2: Manual Log Inspection
Before automated analysis, I performed a manual check on the HTTP logs to identify suspicious headers or unusual destination paths.
![Manual Log Inspection](http_log_check.png)
*Inspecting the top entries of http.log to identify initial web-based indicators.*

### Phase 3: RITA Database Import
Zeek logs were imported into the RITA database to calculate connection intervals and statistical frequency.
![RITA Data Import](rita_import.png)
*Importing generated Zeek logs into the 'asyncrat' database for analysis.*

### Phase 4: Beaconing & Threat Correlation
Using RITA's statistical engine, I identified hosts showing repetitive connection patterns (Beacons).
![Beaconing Analysis Results](beacon_analysis.png)
*Final analysis results showing Beaconing likelihood for host 10.3.14.101.*

---

## 4. Key Findings & Indicators of Compromise (IoC)

| Indicator | Type | Observations |
| --- | --- | --- |
| **10.3.14.101** | Internal IP | Primary source of suspicious beaconing activity. |
| **AsyncRAT.pcap** | File Name | Captured traffic confirms signature of AsyncRAT C2 communication. |
| **Multiple Destination IPs** | C2 Nodes | High-frequency connections observed to external addresses. |
| **Beacon Score** | Statistical | Observed patterns consistent with automated malware heartbeats. |

---

## 5. Analysis & Impact
* **Prevalence Analysis:** The analysis confirms that host **10.3.14.101** is communicating with external infrastructure in a rhythmic pattern, bypassing traditional signature-based detection.
* **Verdict:** **Confirmed True Positive (TP)** — Active C2 communication detected.
* **Impact:** **High** - Risk of full host compromise and potential data exfiltration through the established C2 channel.

---

## 6. Recommendations & Remediation

### Immediate Response
1. **Host Isolation:** Immediately isolate host `10.3.14.101` from the network to prevent further C2 commands.
2. **Traffic Blocking:** Blacklist the destination IPs found in the RITA analysis at the perimeter firewall.
3. **Endpoint Scan:** Perform a deep forensic scan on the affected host for AsyncRAT persistence (e.g., Scheduled Tasks, Run Keys).

### Long-term Hardening
1. **Automation:** Integrate Zeek and RITA into the SOC pipeline for daily automated beaconing reports.
2. **Egress Filtering:** Implement strict outbound firewall rules (Deny All, Permit Specific).
3. **Threat Intel:** Feed identified IoCs back into the SIEM for future correlation.

---
[⬅️ Back to Writeups](./README.md)
