# 🔍 Digital Forensics & Investigation Cheat-Sheet

This cheat-sheet serves as a quick reference for file system analysis, artifact recovery, and digital investigation techniques.

This document is designed for **SOC analysts**, **junior digital forensics investigators**, and **security trainees** who need fast, reliable forensic references during investigations.

---

## 📂 File System Fundamentals (NTFS & FAT)

| Artifact | Description | Purpose in Investigation |
| :--- | :--- | :--- |
| **MBR** | Master Boot Record | Identify partition offsets and boot-related artifacts. |
| **MFT** | Master File Table | Core NTFS structure containing file metadata and timestamps. |
| **$LogFile** | NTFS Journal | Tracks file system changes (creation, deletion, modification). |
| **Inodes** | Linux File Metadata | Identifies file ownership, permissions, and timestamps in EXT4. |

---

## 🛠️ WinHex & Manual Disk Analysis

* **Sector Size:** Typically 512 bytes.
* **Common File Signatures (Magic Numbers):**
  * `4D 5A` → Windows Executable (.exe)
  * `FF D8 FF` → JPEG Image
  * `50 4B 03 04` → ZIP / Office Open XML
  * `7F 45 4C 46` → Linux Executable (ELF)

---

## 💻 Windows Registry Forensics (Evidence of Execution)

Key registry locations used to identify user activity and persistence mechanisms:

- **User Activity:**  
  `NTUSER.DAT\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs`

- **Auto-Run (Persistence):**  
  `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`

- **System Identification:**  
  `SYSTEM\CurrentControlSet\Control\ComputerName`

- **Program Execution Evidence:**  
  `C:\Windows\Prefetch`

---

## 📱 Mobile Forensics (Android)

* **Logical Acquisition:** Extraction of visible user data (messages, contacts).
* **Physical Acquisition:** Bit-by-bit image including deleted and unallocated space.
* **Analysis Tool:** **Autopsy** for ingesting images and keyword-based investigation.

---

## 🌐 OSINT Investigation Workflow

1. **Username Enumeration:** Cross-platform checks using *Sherlock*.
2. **Image Analysis:** Reverse image searches via *Google Images* or *Yandex*.
3. **Email Intelligence:** Breach verification using *HaveIBeenPwned*.
4. **Domain & IP Analysis:** Use *Whois* and *VirusTotal* for reputation and ownership.

---

## 💡 Practical Investigation Tips

> Always verify the **hash value** (MD5 / SHA256) of digital evidence before and after analysis to ensure data integrity.

> Maintain a clear **investigation timeline** and **chain of custody** to ensure evidence admissibility and forensic soundness.

---

[⬅️ Back to Main Portfolio](../../README.md)
