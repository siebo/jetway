import argparse
import subprocess

# networksetup -getairportpower <device name>
# networksetup -setairportpower <device name> <on off>

# networksetup -getairportnetwork <device name>
# networksetup -setairportnetwork <device name> <network> [password]

# networksetup -listpreferredwirelessnetworks <device name>
# networksetup -addpreferredwirelessnetworkatindex <device name> <network> <index> <security type> [password]
# networksetup -removepreferredwirelessnetwork <device name> <network>
# networksetup -removeallpreferredwirelessnetworks <device name>

# Scan for networks
# /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s

parser = argparse.ArgumentParser()
parser.add_argument("-l","--list", help="list the available networks")
parser.add_argument("-j","--join", help="join a network")
parser.add_argument("-f","--forget", help="remove a preferred network")
parser.add_argument("noun", help="target")
args = parser.parse_args()
print args
