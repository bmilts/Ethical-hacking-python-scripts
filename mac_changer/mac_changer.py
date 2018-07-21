#!/usr/bin/env python

import subprocess

# Get info from user for command arguments
import optparse

# Create parser object to handle user input
parser = optparse.OptionParser()

# User arguments to expect from user (-i or interface acceptable arguments)
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")

# Understand user arguments
(options, arguments) = parser.parse_args()

# User input
interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# Run linux commands through subprocess using default
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

# Run linux commands through subprocess more securely using a list
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])