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
 reverse shell and remote thread strings

## Why use it?
Security analysts use YARA rules to:
- Scan suspicious files without opening them
- Identify malware families from known string patterns
- Hunt for threats across multiple files at once
- Build custom detection rules for new malware

## How to Run It
```
python yarascanner.py [rules.yar] [file_to_scan]
```

## Example
```
python yarascanner.py rules.yar suspicious.txt
```

## Expected Output
```
Loading rules from rules.yar...
Scanning suspicious.txt...

⚠️  MATCHES FOUND in suspicious.txt

Rule: DetectRansomware
Description: Detects common ransomware strings
Severity: high
Matched Strings:
 Identifier: $a
 Matched: bitcoin

 Identifier: $b
 Matched: encrypt
```

## How to Add New Rules
Open `rules.yar` and follow this template:

```yara
rule RuleName {
   meta:
       description = "What this rule detects"
       author = "Your name"
       severity = "high/medium/low"

   strings:
       $a = "suspicious string" nocase
       $b = "another string" nocase

   condition:
       2 of them
}
```

## Tools Used
- Python
- yara-python
- YARA rule language