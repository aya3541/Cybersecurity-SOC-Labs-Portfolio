# **Technical Analysis Report: Lumma Stealer Data Exfiltration**

## **1. Executive Summary**
This report details the network forensic investigation of a **Lumma Stealer** malware infection. The objective was to analyze raw network traffic to identify Command & Control (C2) infrastructure, track communication patterns, and confirm data exfiltration.

* **Analysis Tool:** Zeek Network Security Monitor
* **Methodology:** Traffic Analysis & Protocol Inspection
* **Case Status:** Critical - Confirmed Data Exfiltration

---

## **2. Phase I: Environment Setup & Log Generation**
The investigation began by processing raw PCAP artifacts into structured, queryable logs using Zeek. This allows for deep inspection of specific protocols such as DNS and HTTP.

![Environment Setup](./Screenshots/01-env-setup.png)

> **Technical Observation:** The generation of `dns.log`, `http.log`, and `conn.log` provides a comprehensive view of the network layer, enabling the isolation of malicious traffic from legitimate noise.

---

## **3. Phase II: C2 Infrastructure Identification**
By analyzing DNS queries, I identified active communication with suspicious Top-Level Domains (TLDs) that are frequently utilized by Lumma Stealer for evasion.

![C2 Identification](./Screenshots/02-dns-c2-detection.png)

> **Indicator of Compromise (IOC):** The domain **`possuhb.cyou`** was identified as a primary Command & Control (C2) node. The high frequency of lookups to this domain indicates an active infection.

---

## **4. Phase III: Traffic Flow & Beaconing Patterns**
Analyzing the `conn.log` allowed for the identification of the communication flow between the internal victim and the external threat actor.

* **Victim Endpoint:** `10.1.14.101`
* **External Adversary:** `174.138.43.121`

![Traffic Flow](./Screenshots/03-traffic-flow.png)

> **Technical Detail:** The logs show persistent TCP connections to the remote IP. The pattern of these connections suggests **Beaconing** activity, where the malware periodically checks in with the C2 server for tasking.

---

## **5. Phase IV: Confirmed Data Exfiltration**
The final stage of analysis confirmed the impact of the attack. Inspection of HTTP traffic revealed the exfiltration of sensitive user data.

![Exfiltration Evidence](./Screenshots/04-data-exfiltration.png)

> **Deep Packet Inspection (DPI):** The captured **HTTP POST** requests to the `/api/set_agent` endpoint provide definitive proof of data theft. The URI parameters indicate the exfiltration of credentials and session tokens from **Google Chrome** and **Microsoft Edge**.

---

## **6. Phase V: MITRE ATT&CK Mapping & Investigative Logic**
To contextualize the technical findings, I mapped the observed **Lumma Stealer** behaviors to the MITRE ATT&CK framework. This ensures the investigation follows a globally recognized methodology.

### **Part A: Credential Theft & C2 Communication**
In this stage, the focus was on how the malware handles the stolen data and communicates with its controller.

![Lumma Mapping - Part 1](./Screenshots/lumma-mapping-1.png)

* **Technique: [Credentials from Web Browsers (T1555.003)](https://attack.mitre.org/techniques/T1555/003/):** The analysis confirmed that the malware specifically targeted local database files to extract saved credentials and cookies.
* **Technique: [Application Layer Protocol (T1071.001)](https://attack.mitre.org/techniques/T1071/001/):** The use of HTTP POST requests for exfiltration was mapped to this technique, highlighting the use of standard web protocols to blend in with legitimate traffic.

### **Part B: System Discovery & Environment Reconnaissance**
Before the exfiltration phase, the malware was observed gathering intelligence about the host environment.

![Lumma Mapping - Part 2](./Screenshots/lumma-mapping-2.png)

* **Technique: [System Information Discovery (T1082)](https://attack.mitre.org/techniques/T1082/):** The logs indicated queries for hardware specifications and OS details, used by the malware to fingerprint the victim's machine.

---

## **7. Conclusion & Mitigation**
The analysis confirms a successful deployment of Lumma Stealer with high-impact data exfiltration. 

### **Recommendations:**
1.  **Host Isolation:** Isolate `10.1.14.101` from the production network.
2.  **Network Blocking:** Blacklist IP `174.138.43.121` and block all `.cyou` TLD traffic at the firewall level.
3.  **Credential Reset:** Force a password reset for all browser-synced accounts (Google/Microsoft) associated with the victim machine.

---
