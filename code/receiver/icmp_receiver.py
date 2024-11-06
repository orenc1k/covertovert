from scapy.all import ICMP, IP, sniff


def control_ttl(packet):
    # Control coming ICMP packets
    if packet.haslayer(ICMP) and packet[IP].ttl == 1:
        packet.show()


def listeing_icmp():
    # Listening ICMP packets with TTL=1
    sniff(filter="icmp", prn=control_ttl)


if __name__ == "__main__":
    listeing_icmp()
