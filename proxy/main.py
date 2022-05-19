#!/usr/bin/env python
import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.accept()

if __name__ == "__main__":
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()