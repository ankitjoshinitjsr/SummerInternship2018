#!/usr/bin/python

print("content-type: text/html")
print("")


import commands as sp
import cgi
import cgitb
import socket
from contextlib import closing


def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

port=find_free_port()
form=cgi.FieldStorage()
user=form.getvalue('u')
print("<iframe name='i1' height='300' width='800'></iframe>")
sp.getoutput("sudo docker run -dit -p {0}:4200 --name {1} paas:latest".format(port,user))
print("<a href='http://192.168.43.50:{}' target='i1'>Start</a>".format(port))
 
