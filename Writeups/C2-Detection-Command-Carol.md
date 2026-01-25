
# Case Study: Network Hunting & C2 Detection (Command & Carol)

## 1. Executive Summary

This report documents a proactive threat hunting investigation focused on identifying **Command and Control (C2)** communication within captured network traffic. Using **RITA (Real Intelligence Threat Analytics)** and **Zeek logs**, I analyzed large-scale PCAP data to detect beaconing patterns, unauthorized long-duration connections, and communication with known malicious infrastructures.

* **Objective:** Identify compromised internal hosts communicating with external C2 servers.
* **Key Finding:** Detected high-likelihood beaconing activity to `malhare.net` and `rabbithole.malhare.net`.
* **Attack Vector:** Automated beaconing from internal hosts to C2 domains.
* **Impact:** Potential unauthorized system control and data exfiltration.

---

## 2. Investigation Context

* **Platform:** Network Security Monitoring (NSM) Environment
* **Analysis Tools:**
* `RITA`: Beaconing detection & statistical analysis
* `Zeek`: Network flow & connection logging
* `Wireshark`: Packet-level inspection


* **Artifacts:** `rita_challenge.pcap`, Zeek Connection Logs (`conn.log`)
* **Methodology:** Statistical Analysis & Beacon Detection

---

## 3. Technical Investigation & Methodology

### Phase 1: PCAP to Zeek Conversion

Raw PCAPs were converted into structured Zeek logs to enable RITA processing.

**Command Executed:**

```bash
zeek readpcap pcaps/rita_challenge.pcap zeek_logs/challenge_analysis

```

* **Focus:** PCAP parsing, Zeek log generation

### Phase 2: RITA Import & Analysis

Zeek logs were imported into RITA's database to correlate connection intervals and calculate beacon scores.

**Commands Executed:**

```bash
# Import logs into RITA database
rita import --logs ~/zeek_logs/challenge_analysis/ --database challenge_db

# View analysis results
rita view challenge_db

```

* **Focus:** Beacon scoring, statistical threat correlation

### Phase 3: Beaconing & Threat Analysis

Used RITA filters to identify hosts with high **Beacon Likelihood**.

**Search Filter Used:**

```bash
/beacon > 0.70 & fqdn = "rabbithole.malhare.net" | sort duration desc

```

* **Focus:** Automated C2 detection, host-level anomaly identification

---

## 4. Key Findings & Indicators of Compromise (IoC)

| Indicator | Type | Observations |
| --- | --- | --- |
| `malhare.net` | C2 Domain | Communicating with multiple internal hosts simultaneously. |
| `rabbithole.malhare.net` | C2 FQDN | High-frequency connections from host `10.0.0.13`. |
| Port `4444` | Non-standard Port | Unauthorized traffic observed (typical for C2/Metasploit). |
| Beacon Score | > 0.70 | Indicates highly regular automated connections. |

* **Focus:** IoC identification, domain & port correlation

---

## 5. Analysis & Impact

* **Prevalence Analysis:** Widespread communication with suspicious domains indicates potential worm or mass infection across the network.
* **Connection Behavior:** Host `10.0.0.13` shows significant C2 traffic, confirming active persistence.
* **Verdict:** **True Positive (TP)** — Confirmed active C2 infrastructure.

**CIA Impact:**

| Property | Impact |
| --- | --- |
| **Confidentiality** | **High** - Risk of data exfiltration via established C2 tunnel |
| **Integrity** | **Medium** - Potential for further command execution on compromised hosts |
| **Availability** | **Low** - Core services not disrupted but network bandwidth is consumed |

---

## 6. Strategic Recommendations

### Immediate Response

1. **Network Block:** Blacklist `malhare.net` and associated IPs at firewall and DNS level.
2. **Host Isolation:** Isolate `10.0.0.13` and other compromised hosts for forensic imaging and analysis.
3. **Process Audit:** Review suspicious processes (e.g., `PowerShell`, `Netcat`) on affected hosts.

### Long-term Hardening

1. **NSM Deployment:** Continuous monitoring using `Zeek` & `RITA` for automated beacon detection.
2. **Egress Filtering:** Restrict outbound traffic to known-good ports and implement a secure web proxy.
3. **Threat Intel Integration:** Feed real-time threat intelligence into SIEM/EDR to flag known malicious IPs.

* **Focus:** Network hardening, threat intelligence integration, and automated response.

---
[⬅️ Back to Writeups](./README.md)


