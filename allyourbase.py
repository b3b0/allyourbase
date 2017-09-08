import time
import sys
import os
from scapy.all import *

def wazuh():
    os.system('echo "ALLYOURBASE" >> /var/log/auth.log')
    print("IT HAS BEEN DONE")

wazuh()
