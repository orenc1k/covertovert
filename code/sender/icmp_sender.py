from scapy.all import ICMP, IP, send


def icmp_handler(dest):
    # Send ICMP packet
    send(IP(dst=dest, ttl=(1, 1)) / ICMP())


if __name__ == "__main__":
    icmp_handler(dest="receiver")
