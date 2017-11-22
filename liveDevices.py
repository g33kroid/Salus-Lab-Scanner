import subprocess
from termcolor import colored
import threading

live_ips = []
threads = []
def update_live(ip):
    global live_ips
    live_ips.append(ip)
    return

def getInterfaceIPs(ip24):
    interface_ips = []
    ip = ip24.split(".")
    ip = ip[0]+"."+ip[1]+"."ip[2]+"."
    for i in range(0,255):
        tmp = ip+str(i)
        interface_ips.append(tmp)
    return interface_ips

def pinger(ip):
    result = subprocess.check_output('ping -c 3 '+ip+' | grep "3 received"; exit 0',stderr=subprocess.STDOUT,shell = True)
    if result == "":
        return
    else :
        update_live(ip)
        print colored("[+] "+ip+"\t"+"is live",green)
    return

def scanLiveIPs(wifi,ether):
    wifiIP = getInterfaceIPs(wifi)
    etherIP = getInterfaceIPs(ether)
    if(len(wifiIP) > 0):
        for wip in wifiIP:
            t = threading.Thread(target=pinger, args(wip,))
            t.setName(wip)
            global threads
            threads.append(t)
            t.start()
            t.join()
    if(len(etherIP)>0):
        for eip in etherIP:
            t = threading.Thread(target=pinger,args(eip,))
            t.setName(eip)
            global threads
            threads.append(t)
            t.start()
            t.join()
    return

def runningCheck():
    runningCount = 0
    for t in threads:
        if not t.isAlive():
            continue
        else:
            print colored("[-] Still Scanning IP : "+ t.getName())
            runningCount +=1
    return runningCount

def getLiveIPs():
    threadPool = len(threads)
    runningCount = runningCheck()
    while runningCount != 0:
        runningCount = runningCheck()
    return live_ips