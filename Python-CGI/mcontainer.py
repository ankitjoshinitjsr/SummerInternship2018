#!/usr/bin/python2
import commands
import cgi

print("Content-Type: text/html")


import socket
from contextlib import closing

def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

Count=cgi.FormContent()['n'][0]
Image=cgi.FormContent()['image'][0]
Id=cgi.FormContent()['id'][0]

k=0
#Runs all the containers
while k<int(Count):
        port=find_free_port()
	commands.getoutput("sudo docker run -dit -p {3}:4200 --name={1}{2}.centos {0}".format(Image,k,Id,port))
	k+=1
print "location: dockermanage.py"
print


