#!/usr/bin/env python
import netfilterqueue
from scapy.all import *



def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    print(packet.get_payload)
    packet.accept() #packet.drop # doesn't allow packet to flow

if __name__ == "__main__":
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
    