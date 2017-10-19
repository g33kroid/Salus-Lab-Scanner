import subprocess
from termcolor import colored

def get_assigned_ip():
    #Checking the Wifi Card and Ethernet for any IP Address

    ethernet = subprocess.check_output('ifconfig eth0 | grep inet | cut -d " " -f10 ',shell = True)
    wifi = subprocess.check_output('ifconfig wlan0 | grep inet | cut -d " " -f10 ',shell= True)

    if(ethernet == "" and wifi == ""):
        print colored("[x] No IP assigned .... Check Internet Connection ",'red')
    else:

        ip_ether = str(ethernet).split("\n")
        print colored("Ethernet IP : "+ ip_ether[0],'yellow')

        ip_wifi = str(wifi).split("\n")
        print colored("Wifi IP : "+ ip_wifi[0],'yellow')
    return ip_ether[0] , ip_wifi[0]
