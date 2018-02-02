import nmap
from database import * 

nm = nmap.PortScanner()


def ScanIP(ip):
    scan = nm.scan(ip, arguments= '-A -Pn -O -sV')
    profile(ip,scan)
    if scan["scan"][ip] != "" :
        print('----------------------------------------------------')
        print('Host : ' + ip )
        print('State : '+ scan["scan"][ip].state())

        if(scan["scan"][ip]["tcp"]!= ""):
            for port in scan["scan"][ip]['tcp']:
                thisDict = scan["scan"][ip]['tcp'][port]
                print 'Port ' + str(port) + ': ' + thisDict['product'] + ', v' + thisDict['version']

        if scan["scan"][ip].has_key('osclass'):
            for osclass in scan["scan"][ip]['osclass']:
                print('OsClass.type : '+osclass['type'])
                print('OsClass.vendor :'+osclass['vendor'])
                print('OsClass.osfamily : '+ osclass['osfamily'])
                print('OsClass.osgen : '+ osclass['osgen'])
                print('OsClass.accuracy : ' +osclass['accuracy'])
                print('')

        if scan["scan"][ip].has_key('osmatch'):
            for osmatch in scan["scan"][ip]['osmatch']:
                print('osmatch.name : '+ osmatch['name'])
                print('osmatch.accuracy : ' + osmatch['accuracy'])
                print('osmatch.line : '+ osmatch['line'])
                print('')

        if scan["scan"][ip].has_key('fingerprint'):
            print('Fingerprint : '+ scan["scan"][ip]['fingerprint'])

