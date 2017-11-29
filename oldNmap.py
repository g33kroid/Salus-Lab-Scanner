import subprocess
from termcolor import colored

ip_list = ""
def scan_mode():
    try:
        # For Debugging Purposes
        # mode = raw_input("Do you want Basic scan (b) or Aggressive Scan (a) : ")
        mode = 'a'
        return mode
    except(KeyboardInterrupt,SystemExit):
        print colored("\nKeyboard Interrupt Detected","red")
        print colored("\nExiting")
        exit()

def IPs(mode,ether,wifi):
    try:
        #This Block for Single IP Testing Purposes
        if(mode == "s"):
            global ip_list
            data = raw_input("Enter IP : ")
            ip_list = data
            return ip_list
        elif(mode == "r"):
            assigned_ip = ""
            if(ether == ""):
                assigned_ip = wifi.split(".")
                assigned_ip = assigned_ip[0]+"."+assigned_ip[1]+"."+assigned_ip[2]+"."+"0-255"
            elif(wifi == ""):
                assigned_ip = ether.split(".")
                assigned_ip = assigned_ip[0]+"."+assigned_ip[1]+"."+assigned_ip[2]+"."+"0-255"
            elif (ether != "" or wifi != ""):
                print colored("2 Wifi Connections Found",'white')
            IPr = assigned_ip
            IPrange = IPr.split("-")
            IPstart = IPrange[0]
            IPstarts = IPstart.split(".")
            IPstart = int(IPstarts[-1])
            IPend = int(IPrange[1])
            print colored("[-] Scanning the Full Range 255 IPs",'yellow')
            IParray = []

            for i in range(IPstart,IPend+1):
                ip = IPstarts[0]+"."+IPstarts[1]+"."+IPstarts[2]+"."+str(i)
                #print(ip)
                IParray.append(ip)
            return IParray
        else:
            print colored("[x] Scan Mode Can't be Detmined",'red')
            exit()
    except(KeyboardInterrupt,SystemExit):
        print colored("\n[x] Keyboard Interrupt Detected , Exiting",'red')
        exit()

def ip_mode(ether,wifi):
    try:
        ip_modes = 'r'
    except(KeyboardInterrupt,SystemExit):
        print colored("\n[!] System Exit determined",'red')
        exit()

    ip_list = IPs(ip_modes,ether,wifi)
    # This Block for Debugging Purposes
    # print colored("[+]---- IPs to be Scanned ----",'yellow')
    # if ip_mode == "r":
    #     for i in ip_list:
    #         print(i)
    # else:
    #     print(ip_list)
    return ip_list , ip_modes

def nmap_scan(ip,scan_mode,ip_mode):
    # Single IP Scanning for Debugging Purposes
    if(ip_mode == 's'):
        print colored("[+] Scanning Single IP : "+ip,'white')
        if (scan_mode == 'b'): # Single IP Basic Scan
            print colored("[-] Scanning Started for : "+ip,'yellow')
            result = subprocess.check_output("nmap -Pn "+ip , shell=True)
            print colored("[+] Scan Complete Printing Results",'green')
            result = str(result).split("\n")
            for i in result:
                print(i)
        elif(scan_mode == 'a'): #Single IP Aggressive Scan
            #print colored("[x] Under Implementation",'red')
            print colored("[-] Scanning Started for : "+ip,'yellow')
            result = subprocess.check_output("nmap -Pn -A -sV -O "+ip , shell=True)
            print colored("[+] Scan Complete Printing Results",'green')
            result = str(result).split("\n")
            for i in result:
                print(i)

        else:
            print colored("[x] Error",'red')
    elif(ip_mode == 'r'):
        print colored("[-] Scan Started",'white')
        for i in ip:
            print colored("[-] Starting Scan for : " + i ,'yellow')
            result = subprocess.check_output("sudo nmap -Pn -A -sV -O "+i , shell=True)
            print colored("[+] Scan Complete Printing Results",'green')
            result = str(result).split("\n")
            for i in result:
                print(i)
    else:
        print colored("[x] Internal Error IP_Mode is wrong",'red')
