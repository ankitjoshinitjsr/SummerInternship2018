#!/usr/bin/python36

print("content-type: text/html")
print("")

import cgi
import subprocess as sp
data=cgi.FieldStorage()
usrName=data.getvalue('usr')
Cip=data.getvalue('Cip')
Pass=data.getvalue('Pass')
dirName=data.getvalue('dir')
size=data.getvalue('size')
print("<pre>")
sp.getoutput("sshpass -p blackhat ssh -o stricthostkeychecking=no -l root 192.168.43.190 mkdir /nfs/{0}".format(usrName))

sp.getoutput("sshpass -p blackhat ssh -o stricthostkeychecking=no -l root 192.168.43.190 lvcreate --size {0}M --name {1} nfs".format(size,usrName))

sp.getoutput("sshpass -p blackhat ssh -o stricthostkeychecking=no -l root 192.168.43.190 mkfs.ext4 /dev/nfs/{0}".format(usrName))


sp.getoutput("sshpass -p blackhat ssh -o stricthostkeychecking=no -l root 192.168.43.190 mount /dev/nfs/{0} /nfs/{0}".format(usrName))

sp.getoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mkdir /media/{2}".format(Pass,Cip,dirName))

x=sp.getstatusoutput("sshpass -p blackhat scp -o stricthostkeychecking=no  root@192.168.43.190:/etc/exports /nfs/")


x="/nfs/{0}/{1}	{2}(rw,no_root_squash)".format(usrName,dirName,Cip)

sp.getoutput("sudo chown apache /nfs/exports")

f=open('/nfs/exports','a')
f.write(x+'\n')
f.close()

x=sp.getoutput("sshpass -p blackhat scp -o stricthostkeychecking=no /nfs/exports  root@192.168.43.190:/etc/")
print(x)

x=sp.getstatusoutput("sshpass -p blackhat scp -o stricthostkeychecking=no  root@192.168.43.190:/etc/fstab /nfs/")

x="/dev/nfs/{0}	 /nfs/{0}  ext4  defaults  0 0".format(usrName)

sp.getoutput("sudo chown apache /nfs/fstab")

f=open('/nfs/fstab','a')
f.write(x+'\n')
f.close()

x=sp.getoutput("sshpass -p blackhat scp -o stricthostkeychecking=no /nfs/fstab  root@192.168.43.190:/etc/")


x=sp.getstatusoutput("sshpass -p blackhat ssh -o stricthostkeychecking=no -l root 192.168.43.190 exportfs -v")
print(x[0])

x=sp.getstatusoutput("sshpass -p blackhat ssh -o stricthostkeychecking=no -l root 192.168.43.190 systemctl restart nfs")
print(x[0])

x=sp.getstatusoutput("sshpass -p blackhat ssh -o stricthostkeychecking=no -l root 192.168.43.190 systemctl enable nfs")
print(x[0])

x=sp.getoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mount 192.168.43.190:/nfs/{3} /media/{2}".format(Pass,Cip,dirName,usrName))
print(x)

x=sp.getstatusoutput("sshpass -p {0} scp -o stricthostkeychecking=no  root@{1}:/etc/fstab /nfs/".format(Pass,Cip))
print(x)

x="192.168.43.190:/nfs/{0}  /media/{1}  nfs4  defaults  0 0".format(usrName,dirName)
print(x)

sp.getoutput("sudo chown apache /nfs/fstab")

f=open('/nfs/fstab','a')
f.write(x+'\n')
f.close()

x=sp.getoutput("sshpass -p {0} scp -o stricthostkeychecking=no /nfs/fstab  root@{1}:/etc/".format(Pass,Cip))
print(x)
print("</pre>")
