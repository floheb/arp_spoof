# Basic ARP Work

## Disclaimer

**This tool is intended strictly for legal and educational purposes. Unauthorized use may violate laws and regulations regarding network security and privacy.**

## Overview

This is a minimalist library demonstrating the basic use of Scapy for ARP spoofing on a single target. It allows monitoring network activity by intercepting DNS requests and identifying the IPs a target communicates with.

## Features

- **ARP Spoofing**: Redirect network traffic by poisoning the ARP cache.
- **IP Resolution**: Convert domain names to IP addresses.
- **Traffic Monitoring**: Capture and display network packets.
- **Configuration Management**: Store network settings in a JSON file.

## Installation

Clone the repository and set up a virtual environment:

```sh
git clone https://github.com/floheb/arp_spoof
cd arp_spoof
python -m venv env
source env/bin/activate 
pip install -r requirements.txt
```

## Usage

Run the scripts with elevated privileges:

```sh
sudo env/bin/python arp_spoof.py
sudo env/bin/python show_traffic.py
```

### Important: Enable IP Forwarding

If ARP spoofing does not work, ensure IP forwarding is enabled:

#### Linux:
```sh
echo 1 > /proc/sys/net/ipv4/ip_forward
```

#### macOS:
```sh
sudo sysctl -w net.inet.ip.forwarding=1
```

## Purpose

This tool is designed to monitor basic DNS requests of a target or determine the IPs it communicates with. You can then resolve these IPs using (paste the output in the beginning of the file):

```sh
python resolve_ip.py <IP>
```

## Enhancements and Future Improvements

- **Make ARP Spoofing stealthier**: Instead of sending ARP packets every second, randomize the intervals to be less spotted.
- **Multiple Targets**: Extend ARP spoofing capabilities to multiple devices. (not that usefull for this first step)
