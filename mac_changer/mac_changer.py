#!/usr/bin/env python

import subprocess

# Get info from user for command arguments
import optparse

def get_arguments():
    # Create parser object to handle user input
    parser = optparse.OptionParser()

    # User arguments to expect from user (-i or interface acceptable arguments)
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")

    # Understand and return user arguments
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a mac address, use --help for more info.")

    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    # Run linux commands through subprocess more securely using a list
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
# Pass user input via options.interface
# change_mac(options.interface, options.new_mac)

# Return output to check if mac is changed
subprocess.check_output(["ifconfig", options.interface])


