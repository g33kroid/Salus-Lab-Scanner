import couchdb
from termcolor import colored 

def profile(ip,scan):
    couch = couchdb.Server()
    name = "machine_"+ip.split(".")[-1]
    try:
        db = couch[name]
        db.save(scan)
        print colored("Scan Saved",'white')
    except couchdb.http.ResourceNotFound:
        db = couch.create(name)
        print colored (ip + " Profile Created",'yellow')
        db.save(scan)
        print colored("Scan Saved",'white')
    return 