rule DetectRansomware {
   meta:
       description = "Detects common ransomware strings"
       author = "Joel"
       severity = "high"
   strings:
       $a = "bitcoin" nocase
       $b = "encrypt" nocase
       $c = "ransom" nocase
       $d = "YOUR FILES HAVE BEEN ENCRYPTED"
       $e = "cmd.exe" nocase
   condition:
       2 of them
}


rule DetectRAT {
   meta:
       description = "Detects common Remote Access Trojan strings"
       author = "Joel"
       severity = "high"
   strings:
       $a = "keylogger" nocase
       $b = "screenshot" nocase
       $c = "RemoteThread" nocase
       $d = "backdoor" nocase
       $e = "reverse shell" nocase
   condition:
       2 of them
}