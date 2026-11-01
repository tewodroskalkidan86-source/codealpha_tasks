from scapy.all import IP, ICMP, TCP, UDP

packet = IP(src="192.168.1.10",
            dst="192.168.1.20") / ICMP()

print("=== Packet Inspector ===")

if IP in packet:
    print("Source IP:", packet[IP].src)
    print("Destination IP:", packet[IP].dst)

if ICMP in packet:
    print("Protocol: ICMP")
elif TCP in packet:
    print("Protocol: TCP")
elif UDP in packet:
    print("Protocol: UDP")
else:
    print("Protocol: Other")