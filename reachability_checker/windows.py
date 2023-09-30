# This program is used to ping ip address or hostname of devices.
# Just pass the file containing the ip address to this program.

from colorama import Style, Fore
import subprocess, os
from time import sleep
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <list of ip>")
    exit(1)

os.system('cls')
hosts = []
with open(sys.argv[1], 'r') as file:
    contents = file.readlines()
    for content in contents:
        hosts.append(content.replace("\n", ''))

success = Fore.GREEN + "PASS" + Style.RESET_ALL
fail = Fore.RED + "FAIL" + Style.RESET_ALL

while True:
    ping_interval = 5
    print(Fore.BLUE + "#" * 40)
    print(" " * 5 + " Checking Hostname/IP")
    print("#" * 40 + Style.RESET_ALL)
    print()
    for host in hosts:
        try:
            details = subprocess.check_output(f"ping -w 500 -n 1 {host}")
            if "Packets: Sent = 1, Received = 1, Lost = 0 (0% loss)" in details.decode():
                print(f"{host}: \t\t\t" + f"------------> {success}")
        except subprocess.CalledProcessError:
            print(f"{host}: \t\t\t" + f"------------> {fail}")
    sleep(ping_interval)

