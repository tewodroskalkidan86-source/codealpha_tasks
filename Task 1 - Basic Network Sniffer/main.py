def show_menu():
    print("\n=== CodeAlpha Basic Network Sniffer ===")
    print("1. View project information")
    print("2. Analyze example packets")
    print("3. Exit")


def show_information():
    print("\nProject: Basic Network Sniffer")
    print("Language: Python")
    print("Library: Scapy")
    print("Purpose: Learn about network packets")
    print("Safety: Capture only authorized traffic")


def analyze_examples():
    from scapy.all import IP, TCP, UDP, ICMP

    packets = [
        IP() / TCP(),
        IP() / UDP(),
        IP() / TCP(),
        IP() / ICMP(),
        IP() / UDP()
    ]

    counts = {"TCP": 0, "UDP": 0, "ICMP": 0, "Other": 0}

    for packet in packets:
        if TCP in packet:
            counts["TCP"] += 1
        elif UDP in packet:
            counts["UDP"] += 1
        elif ICMP in packet:
            counts["ICMP"] += 1
        else:
            counts["Other"] += 1

    print("\n=== Example Packet Analysis ===")
    for protocol, total in counts.items():
        print(f"{protocol}: {total}")


while True:
    show_menu()
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        show_information()
    elif choice == "2":
        analyze_examples()
    elif choice == "3":
        print("Thank you for using the project!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")