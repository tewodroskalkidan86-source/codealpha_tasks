from scapy.all import sniff, IP, TCP, UDP, ICMP

def show_packet(packet):
    if IP not in packet:
        return

    source = packet[IP].src
    destination = packet[IP].dst

    if TCP in packet:
        protocol = "TCP"
    elif UDP in packet:
        protocol = "UDP"
    elif ICMP in packet:
        protocol = "ICMP"
    else:
        protocol = "Other"

    print("Source IP:", source)
    print("Destination IP:", destination)
    print("Protocol:", protocol)
    print("-" * 30)

print("Waiting to inspect 5 authorized packets...")
sniff(prn=show_packet, count=5, store=False)
print("Capture finished.")