#!usr/bin/env python
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from scapy.layers.l2 import arping, ARP, Ether, srp
from scapy.all import *
import argparse

def scan(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for i in answered:
        client_dict={"IP Address": i[1].psrc, "MAC": i[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list
def print_result(results):
    print("IP\t\t\tMAC Address\n----------------------------------------")
    for i in results:
        print(i["IP Address"] + "\t\t" + i["MAC"])

def get_targets():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP/IP range to scan")
    x = parser.parse_args()
    return x

if __name__ == '__main__':
    target = get_targets()
    print_result(scan(target.target))
