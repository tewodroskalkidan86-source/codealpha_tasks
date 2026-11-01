from scapy.all import IP, ICMP

packet = IP(dst="127.0.0.1") / ICMP()

print("Scapy is working!")
print(packet.summary())