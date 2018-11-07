#!/usr/bin/python36

print("content-type: text/html")
print("")
import os,cgi
import subprocess as sp

data=cgi.FieldStorage()
print(data)
Container_name=data.getvalue('cname')
Image_name=data.getvalue('imgname')
print(imgname+cname)

Docker_status=sp.getoutput("sudo docker run -dit -p 4200:4200 --name {0} {1}".format(cname,imgname))
if Docker_status==0:
   print("<iframe src="http://192.168.43.50:4200" height='300' width='800'></iframe>")

