

#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
    Inspector
    authors: egycondor;Micr0bot

    (C) 2018 Saluslab
 

    TODO:
     ALpha
     * x
     * y
     * z
     Beta:
     * x
"""

# ############
# LIBRARIES #
#############

import urllib  # Check for new versions from the repo
import os
import sys
# Executing, communicating with, killing processes
from subprocess import Popen, call, PIPE
from signal import SIGINT, SIGTERM

################################
# GLOBAL VARIABLES IN ALL CAPS #
################################

# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

REVISION = 88;



def upgrade():
        """
            Checks for new version, prompts to upgrade, then
            replaces this script with the latest from the repo
        """
        try:
            print GR + ' [!]' + W + ' upgrading requires an ' + G + 'internet connection' + W
            print GR + ' [+]' + W + ' checking for latest version...'
            revision = get_revision()
            if revision == -1:
                print R + ' [!]' + O + ' unable to access GitHub' + W
            elif revision > REVISION:
                print GR + ' [!]' + W + ' a new version is ' + G + 'available!' + W
                print GR + ' [-]' + W + '   revision:    ' + G + str(revision) + W
                response = raw_input(GR + ' [+]' + W + ' do you want to upgrade to the latest version? (y/n): ')
                if not response.lower().startswith('y'):
                    print GR + ' [-]' + W + ' upgrading ' + O + 'aborted' + W
                    exit(0)
                    return
                # Download script, replace with this one
                print GR + ' [+] ' + G + 'downloading' + W + ' update...'
                try:
                    sock = urllib.urlopen('https://github.com/egycondor/inspector/raw/master/inspector.py')
                    page = sock.read()
                except IOError:
                    page = ''
                if page == '':
                    print R + ' [+] ' + O + 'unable to download latest version' + W
                    exit(1)

                # Create/save the new script
                f = open('inspector_new.py', 'w')
                f.write(page)
                f.close()

                # The filename of the running script
                this_file = __file__
                if this_file.startswith('./'):
                    this_file = this_file[2:]

                # create/save a shell script that replaces this script with the new one
                f = open('update_inspector.sh', 'w')
                f.write('''#!/bin/sh\n
                           rm -rf ''' + this_file + '''\n
                           mv inspector_new.py ''' + this_file + '''\n
                           rm -rf update_inspector.sh\n
                           chmod +x ''' + this_file + '''\n
                          ''')
                f.close()

                # Change permissions on the script
                returncode = call(['chmod', '+x', 'update_inspector.sh'])
                if returncode != 0:
                    print R + ' [!]' + O + ' permission change returned unexpected code: ' + str(returncode) + W
                    exit(1)
                # Run the script
                returncode = call(['sh', 'update_inspector.sh'])
                if returncode != 0:
                    print R + ' [!]' + O + ' upgrade script returned unexpected code: ' + str(returncode) + W
                    exit(1)

                print GR + ' [+] ' + G + 'updated!' + W + ' type "./' + this_file + '" to run again'

            else:
                print GR + ' [-]' + W + ' your copy of inspector is ' + G + 'up to date' + W

        except KeyboardInterrupt:
            print R + '\n (^C)' + O + ' inspector upgrade interrupted' + W
        exit(0)

def get_revision():
    """
        Gets latest revision # from the GitHub repository
        Returns : revision#
    """
    irev = -1

    try:
        sock = urllib.urlopen('https://github.com/egycondor/inspector/raw/master/inspector.py')
        page = sock.read()
    except IOError:
        return (-1, '', '')

    # get the revision
    start = page.find('REVISION = ')
    stop = page.find(";", start)
    if start != -1 and stop != -1:
        start += 11
        rev = page[start:stop]
        try:
            irev = int(rev)
        except ValueError:
            rev = rev.split('\n')[0]
            print R + '[+] invalid revision number: "' + rev + '"'

    return irev


if __name__ == '__main__':
	try:
		upgrade()

	except KeyboardInterrupt:
       	 	print R + '\n (^C)' + O + ' interrupted\n' + W
  	except EOFError:
        	print R + '\n (^D)' + O + ' interrupted\n' + W
