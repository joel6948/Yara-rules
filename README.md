# YARA Malware Scanner
## What is YARA?
YARA (Yet Another Recursive Acronym) is an industry standard
tool used by security analysts and malware researchers to
identify and classify malware based on pattern matching.
Used by major platforms including VirusTotal, Microsoft
Defender and CrowdStrike.
## What does this tool do?
A Python based YARA scanner that loads detection rules and
scans files for malicious patterns. Reports which rules
triggered, severity level, and the exact strings that matched.
## Malware Families Detected
- **Ransomware** — detects bitcoin payment strings, encryption
 references and ransom demands
- **RAT (Remote Access Trojan)** — detects keylogger, backdoor,
 reverse shell and remote thread