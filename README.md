## Disclaimer
This project is for educational purposes only. The labs were conducted in a controlled environment on my own personal devices (iPhone and Windows Laptop). Unauthorized access to networks or devices is illegal and unethical.
# ARP Spoofing & DNS Analysis Lab

# Repository Structure
* `spoof.py`: The Python script using Scapy to perform the ARP poisoning.
* `Youtube and Google queries.png`: Screenshot showing intercepted DNS traffic when opening the YouTube app.
* `icloud private relay.png`: Screenshot showing the iPhone's attempts to mask traffic via Apple's relay servers.

## Description
This project demonstrates a Man-in-the-Middle (MitM) attack to intercept network traffic. 
Using a Python script (Scapy), I spoofed the ARP table of an iPhone  to route its traffic through my laptop.

## Tools Used
* **Python 3**: Primary scripting language.
* **Scapy**: For packet crafting and sending ARP 'is-at' responses.
* **Wireshark / Npcap**: For capturing and inspecting intercepted traffic.

## Key Observations
* Successfully intercepted DNS queries for YouTube and Apple services.
* Observed iCloud Private Relay (mask.apple-dns.net) traffic.
* Analyzed the impact of network latency during a MitM attack.

## Evidence
### Intercepted YouTube Activity
![YouTube Queries](./Youtube%20and%20Google%20queries.png)
*Figure 1: DNS queries demonstrating visibility into app usage despite encryption.*

### iCloud Private Relay Detection
![iCloud Relay](./icloud%20private%20relay.png)
*Figure 2: Identifying the target's use of Apple's privacy-focused proxy service.*