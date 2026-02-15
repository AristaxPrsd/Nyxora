# AmnesiaLog-Parser v1.1
Lightweight RAM - only log analyzer. Unix - engineered. No Dependencies.
Developer: Aristax | Hardware Platform: HP Compaq 2510p | Engine: Vim

## Overview
AmnesiaLog-Parser is a lightweight, zero-dependency Python utility engineered for advanced network forensics and automated log auditing. The core logic is optimized for high-speed string processing and real-time pattern recognition in Unix-like environments.

## Security Architecture: Volatile Memory Policy
To ensure a zero digital footprint (Anti-Forensics), this tool operates exclusively in volatile memory (RAM). No persistent logs, search history, or session data are written to the physical disk. All processed information is permanently purged upon process termination.

## Technical Specifications
- One-Pass Processing: Linear time complexity (O(n)) for large dataset analysis.
- Pattern Identification: Automated detection of SUCCESS (2xx) and FAIL (4xx/5xx) status signatures.
- IP Radar: Frequency analysis and extraction of target IP addresses from raw data streams.
- Session Identity: Unique RAM-linked session identifiers generated via memory address mapping (No external modules required).

## Deployment & Execution
1. Clone the repository:
   git clone https://github.com/AristaxPrsd/AmnesiaLog-Parser

2. Set execution permissions:
   chmod +x logparser.py

3. Run the engine:
   python3 logparser.py

## Testing Environment
The repository includes 'test-logs.txt', a simulated log file containing various network anomalies and status codes for engine verification.

## Disclaimer
This software is provided for educational and security auditing purposes only. The developer is not responsible for any direct or indirect consequences resulting from the use of this tool.

---
Copyright (c) 2026 Aristax Digital Industries. All Rights Reserved.
"Watch your logs, see the unseen."
