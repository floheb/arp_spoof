# Just ctrl+c ctrl+v the output of the other script (show_traffic.py) 

str_ips = """104.18.27.193
104.199.65.9
95.101.110.32
98.82.157.137"""

def parse_ip(str_ips):
   
    ips = str_ips.split("\n")
    return ips

def get_hostnames(ips):
    from socket import gethostbyaddr
    hostnames = []
    for ip in ips:
        try:
            hostname = gethostbyaddr(ip)[0]
            hostnames.append(hostname)
        except Exception as e:
            hostnames.append(f"Can't resolve {ip}")
    return hostnames

if __name__ == "__main__":
    ips = parse_ip(str_ips)
    hostnames = get_hostnames(ips)
    for ip, hostname in zip(ips, hostnames):
        print(f"{ip} : {hostname}")

        