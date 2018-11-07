#!/usr/bin/python36

print("content-type: text/html")
print("")

import cgitb,cgi
import subprocess as sp
print("<pre>")
x=sp.getoutput("sshpass -p blackhat ssh -o stricthostkeychecking=no -l root 192.168.43.190 ls /nfs/")
print(x)
print("</pre>")
