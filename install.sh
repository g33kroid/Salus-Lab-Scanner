#!/bin/bash



sudo echo "deb https://apache.bintray.com/couchdb-deb stretch main" >> /etc/apt/sources.list

sudo apt-get update

sudo apt-get install couchdb
pip install termcolor couchdb

