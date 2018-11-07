#!/usr/bin/python36
import os
import subprocess as sp
import cgi
print("content-type: text/html")
print("")

data=cgi.FieldStorage()
mFold=data.getvalue('dr')
Size=data.getvalue('size')
print(Size)
os.system("sudo chown apache /dev/sdb")
x=sp.getstatusoutput("sudo echo -e 'n\np\n\n\n+{0}\nw\n' | fdisk /dev/sdb ".format(Size))
print(x)
x=os.system("sudo partprobe /dev/sdb")
print(x)
'''
os.system("sudo mkdir /root/Desktop/{0}".format(mFold))
os.system("sudo mkfs.ext4 /dev/sdb1")
os.system("mount /dev/sdb1 /root/Desktop/{0}".format(mFold))
'''
