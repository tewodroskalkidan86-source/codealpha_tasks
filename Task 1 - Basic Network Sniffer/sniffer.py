# CodeAlpha - Basic Network Sniffer
# Author: Kalkidan Tewodros

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

    print("\nPacket Captured")
    print("Source IP:", source)
    print("Destination IP:", destination)
    print("Protocol:", protocol)
    print("-" * 30)


def start_sniffer():
    print("\n=== CodeAlpha Basic Network Sniffer ===")
    print("Capturing up to 5 authorized packets...")
    print("Press Ctrl+C to stop if needed.")

    try:
        sniff(
            prn=show_packet,
            count=5,
            store=False
        )

        print("\nCapture finished.")

    except PermissionError:
        print("Permission error. Check capture permissions.")

    except KeyboardInterrupt:
        print("\nCapture stopped by user.")


def main():
    while True:
        print("\n=== Main Menu ===")
        print("1. Start Sniffer")
        print("2. Project Information")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            start_sniffer()

        elif choice == "2":
            print("\nProject: Basic Network Sniffer")
            print("Language: Python")
            print("Library: Scapy")
            print("Purpose: Inspect packet metadata")
            print("Use only authorized networks.")

        elif choice == "3":
            print("Thank you for using the project!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()