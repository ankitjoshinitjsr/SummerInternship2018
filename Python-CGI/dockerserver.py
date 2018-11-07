#!/usr/bin/python36

print("content-type: text/html")
print("")

import subprocess as sp
import cgitb
cgitb.enable()
print("""
<h3><marquee><u>Docker Server</u></marquee></h3>
<center>
<table border='1px' >
<tr>
<td color='red'>Installation Status</td>
""")
Install_status=sp.getstatusoutput("sudo rpm -q docker-ce")
if Install_status[0]==0:
   print("<td>Installed</td>")
else:
   print("<td>Not Installed</td>")
print("""
</tr>
<tr>
<td>Install Docker</td>
<td><a href='dockersetup.py'>Setup</a></td>
</tr>
<tr>
<td>Docker Service Status</td>
""")
Docker_status=sp.getoutput("sudo systemctl is-active docker")
if Docker_status=='unknown':
   print("<td>stopped</td>")
else:
   print("<td>running</td>")
print("""
</tr>
<tr>
<td>Start Service</td>
<td><a href='dockerstart.py'>Start</a></td>
</tr>
<tr>
<td>Select Image</td>
<td>
<form name=''>
<select name='imgname'>
""")

Docker_images=sp.getoutput("sudo docker images")

Docker_images1=Docker_images.split('\n')
for d in Docker_images1[1:]:
    image=d.split()
    print("<option>"+image[0]+":"+image[1]+"</option>")

print("""
</select>
</td>
</form>
</tr>
</table>
</center>
""")
