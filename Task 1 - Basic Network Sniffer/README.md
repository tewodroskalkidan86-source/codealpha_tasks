# CodeAlpha Basic Network Sniffer

**Author:** Kalkidan Tewodros  
**Language:** Python  
**Library:** Scapy

## 1. Project Overview

This project is a beginner-friendly network sniffer developed using Python and Scapy. It demonstrates how to inspect network packet metadata, including source IP addresses, destination IP addresses, and protocol types.

## 2. Features

- Captures a limited number of network packets.
- Displays source and destination IP addresses.
- Identifies TCP, UDP, ICMP, and other protocols.
- Provides a simple menu interface.
- Allows the user to stop a capture using Ctrl+C.
- Avoids displaying packet payload contents.

## 3. Requirements

- Python
- Scapy
- Npcap on Windows for packet capture

## 4. How to Run

1. Install Python and Scapy.
2. Install Npcap on Windows.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run:

   `python sniffer.py`

6. Choose an option from the menu.

Packet capture may require appropriate permissions.

## 5. Example Output

```text
Packet Captured
Source IP: [source address]
Destination IP: [destination address]
Protocol: TCP
```

The displayed addresses and protocol depend on the packets observed.

## 6. Safety and Ethical Use

This project is for educational purposes. Capture only network traffic you own or have explicit authorization to inspect. Follow applicable laws and organizational policies.

## 7. Learning Outcomes

Through this project, I practiced Python functions, conditional statements, loops, packet inspection, protocol identification, and the use of Scapy.
