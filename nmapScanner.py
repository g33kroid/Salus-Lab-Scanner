from Scanner import *
import threading
from termcolor import colored
import sys
import os

threads = []


def Scan_IPs(ips):
    #nm = nmap.PortScanner()         # instantiate nmap.PortScanner object
    if(len(ips)> 0):
        for ip in ips:
            t = threading.Thread(target=ScanIP,args=(ip,))
            t.setName(ip)
            global threads
            threads.append(t)
            t.start()
            t.join()
    else:
        print colored("[x] No IPs were given to Scan",'red')
        print colored("[x] System Shuts Down",'red')
