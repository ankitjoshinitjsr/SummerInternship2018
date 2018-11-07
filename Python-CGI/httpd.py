#!/usr/bin/python36

print("content-type: text/html")
print("")

import os
import subprocess
import cgi

data=cgi.FieldStorage()
Ip=data.getvalue('cip')
Pass=data.getvalue('cpass')
status=subprocess.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} yum install httpd -y".format(Pass,Ip))
print(status)
if status!=0:
   print("Error Occured")
else:
   os.system("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} systemctl restart httpd".format(Pass,Ip))
                                                                                                                                                                          print("Running and started successfuly")
