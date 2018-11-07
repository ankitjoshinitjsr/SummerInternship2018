#!/usr/bin/python36
print("content-type: text/html")    
print("")                             

import cgi,cgitb
import subprocess as sp
cgitb.enable(display=0,logdir='/logs',format='text')
form = cgi.FieldStorage()
name = form.getvalue('fname')
print("Name of the user is:",name
sp.getoutput("sshapss -p blackhat ssh -o stricthostkeychecking=no 192.168.43.78 date")
