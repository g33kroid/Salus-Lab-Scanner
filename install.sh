#!/bin/bash


apt-get install curl -y
echo "deb https://apache.bintray.com/couchdb-deb jessie main" >> /etc/apt/sources.list

curl -L https://couchdb.apache.org/repo/bintray-pubkey.asc \
    | sudo apt-key add -

apt-get update

sudo apt-get --no-install-recommends -y install \
    build-essential pkg-config erlang \
    libicu-dev libmozjs185-dev libcurl4-openssl-dev -y


sudo apt-get install couchdb -y
systemctl start couchdb

pip install termcolor couchdb python-nmap

curl http://127.0.0.1:5984/

apt install git -y 

git clone https://github.com/mxamusic/Salus-Lab-Scanner.git ~/Desktop/SalusLabScanner

python ~/Desktop/SalusLabScanner/inspector.py

