from scapy.all import IP, TCP, UDP, ICMP

# Example packets for practice
packets = [
    IP() / TCP(),
    IP() / UDP(),
    IP() / TCP(),
    IP() / ICMP(),
    IP() / UDP()
]

# Keep track of protocol counts
counts = {
    "TCP": 0,
    "UDP": 0,
    "ICMP": 0,
    "Other": 0
}

# Examine each packet
for packet in packets:
    if TCP in packet:
        counts["TCP"] += 1
    elif UDP in packet:
        counts["UDP"] += 1
    elif ICMP in packet:
        counts["ICMP"] += 1
    else:
        counts["Other"] += 1

# Display the results
print("=== Protocol Analysis ===")

for protocol, total in counts.items():
    print(protocol, ":", total)