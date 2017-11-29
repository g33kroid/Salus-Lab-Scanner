import nmap
nm = nmap.PortScanner()


def ScanIP(ip):
    nm.scan(ip, arguments= '-A -Pn -O -sV')
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : ' + ip )
        print('State : '+ nm[host].state())

        for port in nm[ip]['tcp']:
            thisDict = nm[ip]['tcp'][port]
            print 'Port ' + str(port) + ': ' + thisDict['product'] + ', v' + thisDict['version']

        if nm[ip].has_key('osclass'):
            for osclass in nm[ip]['osclass']:
                print('OsClass.type : '+osclass['type'])
                print('OsClass.vendor :'+osclass['vendor'])
                print('OsClass.osfamily : '+ osclass['osfamily'])
                print('OsClass.osgen : '+ osclass['osgen'])
                print('OsClass.accuracy : ' +osclass['accuracy'])
                print('')

        if nm[ip].has_key('osmatch'):
            for osmatch in nm[ip]['osmatch']:
                print('osmatch.name : '+ osmatch['name'])
                print('osmatch.accuracy : ' + osmatch['accuracy'])
                print('osmatch.line : '+ osmatch['line'])
                print('')

        if nm[ip].has_key('fingerprint'):
            print('Fingerprint : '+ nm[ip]['fingerprint'])
