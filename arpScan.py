import subprocess
from termcolor import colored

def arp_scan(ip_ether,ip_wifi):
    live_ips = []
    if(ip_ether != ""):
        ip_ether = ip_ether.split(".")
        ip_ether = ip_ether[0]+"."+ip_ether[1]+"."+ip_ether[2]+".0/24"
        result = subprocess.check_output("sudo arp-scan --interface=eth0 "+ip_ether,shell=True)
        output = str(result).split("\n")
        print colored("[-] Getting Live Machines")
        for i in range (2,len(output)-4):
            print colored("[+] "+output[i],"white")
            ip = output[i].split("\t")
            live_ips.append(ip[0])
    elif(ip_wifi != ""):
        ip_wifi = ip_wifi.split(".")
        ip_wifi = ip_wifi[0]+"."+ip_wifi[1]+"."+ip_wifi[2]+".0/24"
        result = subprocess.check_output("sudo arp-scan --interface=wlan0 "+ip_wifi,shell=True)
        output = str(result).split("\n")
        print colored("[-] Getting Live Machines")
        for i in range (2,len(output)-4):
            print colored("[+] "+output[i],"white")
            ip = output[i].split("\t")
            live_ips.append(ip[0])
    else :
        print colored ("[x] Error .... Can't Get Assigned IP",'red');
    return live_ips
