#!/usr/bin/env python
import subprocess
import optparse
import re

#Change the MAC address
def change_mac(interface, new_mac):
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

#getting input
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface or use '--help' for instructions")
    if not options.new_mac:
        parser.error("Please specify an MAC address or use '--help' for instructions")
    return options

#checks current MAC
def get_current_MAC(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    # Retrieve the MAC
    mac_addy_search_result = re.search(b"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)

    if mac_addy_search_result:
        act_mac = str(mac_addy_search_result.group(0))
        act_mac = act_mac[2:-1]
        return act_mac

    else:
        print("Can not find the MAC address\n")
        exit()

#Runner
if __name__ == '__main__':
    options = get_arguments()
    current_mac = get_current_MAC(options.interface)
    old_mac = current_mac
    change_mac(options.interface, options.new_mac)  # changes MAC
    print("The current MAC is: " + current_mac)
    if old_mac==options.new_mac:
        print("New mac is the same as the old one, it is: " + get_current_MAC(options.interface))
    else:
        print("The new MAC address is: " + get_current_MAC(options.interface))



