# Nyxora v1.3
Lightweight RAM-only log forensic engine. Unix-engineered. No Dependencies. Zero Trace.
Developer: Aristax | Hardware Platform: HP Compaq 2510p | Engine: Vim
## Overview
Nyxora is a high-velocity Python utility engineered for advanced network forensics and automated log auditing. The core logic is optimized for high-speed string processing and real-time pattern recognition in Unix-like environments. Unlike traditional analyzers, it focuses on extreme autonomy and zero-dependency operation.
## Security Architecture: Volatile Memory Policy
To ensure a zero digital footprint and implement anti-forensics protocols, this tool operates exclusively in volatile memory (RAM). No persistent logs, search history, or session data are written to the physical disk. All processed information is permanently purged upon process termination.
## Technical Specifications
 * One-Pass Processing: Linear time complexity O(n) for large dataset analysis ensures high performance on legacy hardware.
 * RPS Analysis Engine: Custom logic to calculate Requests Per Second frequency to detect automated bot activity and DoS/DDoS patterns.
 * Pattern Identification: Automated detection of SUCCESS (200-series) and FAIL (400/500-series) status signatures.
 * IP Radar: Real-time extraction and frequency analysis of target IP addresses from raw data streams.
 * Session Identity: Unique RAM-linked session identifiers generated via memory address mapping using the native id function.
## Deployment and Execution
 1. Clone the repository:
   git clone https://github.com/AristaxPrsd/Nyxora
 2. Set execution permissions:
   chmod +x nyxora.py
 3. Run the engine:
   python3 nyxora.py
## Testing Environment
The engine has been tested in GNU/Linux and BSD environments. It is specifically optimized for low-resource systems and remains fully functional without any external Python modules.
## Disclaimer
This software is provided for educational and security auditing purposes only. The developer is not responsible for any direct or indirect consequences resulting from the use of this tool.
Copyright (c) 2026 Aristax Digital Industries. All Rights Reserved.
Watch your logs, see the unseen.
