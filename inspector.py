from subprocess import *
from connection import *
from Banners import *
from termcolor import colored
from nmap import *
from arpScan import *


welcome_banner()
ether,wifi = get_assigned_ip()
ip_list , ip_modes = ip_mode(ether,wifi)
ip_list = arp_scan(ether,wifi)
scan_modes = scan_mode()
nmap_scan(ip_list,scan_modes,ip_modes)