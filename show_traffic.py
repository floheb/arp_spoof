from scapy.all import sniff, IP
import json

with open("config.json") as config_file:
    config = json.load(config_file)
    interface = config["interface"]
    target_ip = config["ip_target"]


communicating_ips = set()

def show_packet(packet):
    try:
        
        if packet.haslayer(IP):
            ip_layer = packet[IP]  

            src_ip = ip_layer.src
            dst_ip = ip_layer.dst

            if src_ip == target_ip:
                communicating_ips.add(dst_ip)
                print("List of IP who spoke with target_ip : ") 
                # We put that because Scapy's sniff does not always let us deal correctly with the KeyboardInterrupt
                for ip in sorted(communicating_ips):
                    print(ip)
                
            elif dst_ip == target_ip:
                communicating_ips.add(src_ip)
                print("List of IP who spoke with target_ip : ")
                for ip in sorted(communicating_ips):
                    print(ip)

    except Exception as e:
        print(f"Erreur lors du traitement d'un paquet : {e}")

if __name__ == "__main__":
    print("Sniffing traffic... Press Ctrl+C to stop.")
    try:
        sniff(iface=interface, prn=show_packet, store=False)
    except KeyboardInterrupt:
        print("\nCapture stopped.")
        print(f"\nList of IP who spoke with target_ip {target_ip}:")
        