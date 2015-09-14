import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("-l","--list", help="list the available networks")
parser.add_argument("-j","--join", help="join a network")
parser.add_argument("-f","--forget", help="remove a preferred network")
args = parser.parse_args()
print args