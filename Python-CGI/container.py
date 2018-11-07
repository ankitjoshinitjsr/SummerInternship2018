#!/usr/bin/python36

print("content-type: text/html")
print("")

import cgi
import subprocess as sp

print("<h3 color='blue'><marquee><u><b>Container as a service</b></u></marquee></h3>")
print("<center>")
print("<textarea rows='10' cols='100'>")
Docker_images=sp.getoutput("sudo docker images")
print(Docker_images)
print("""
</textarea>
</center><br>
<hr color='red'>
<br>
<center>
<h3>Launch Your Container</h3>
<form action='singlecontainer.py'>
Container Name : <input type='text' name='cname'>
<select name='imgname'>
""")
Docker_images1=Docker_images.split('\n')
for d in Docker_images1[1:]:
    image=d.split()
    print("<option>"+image[0]+":"+image[1]+"</option>")

print("""
</select><br><br>
<input type='submit' value='start' width='15'>
</form><br>
<hr color='red'>
<h3>Launch Multiple Container</h3><br>
<form action='mcontainer.py'>
Select Image Name:
<select name='image'>
<br>
<br/>
""")
Docker_images1=Docker_images.split('\n')
for d in Docker_images1[1:]:
    image=d.split()
    print("<option>"+image[0]+":"+image[1]+"</option>")
print("""
</select>
<br>
<br/>
Enter the Number : <input name='n' />
Unique Id: <input name='id' />
<input type='submit' value='start' />      
</form><br/>
<hr color='red'>
<h3>Create Your own image</h3><br>
<form action='dockerfile.py'>
centos : <input name='os' value='centos' type='radio' /> ubuntu : <input name='os' value='ubuntu' type='radio' /> fedora : <input name='os' value='fedora' type='radio' />
<br/><br/>
<b><u>Choose the Services Needed:</u></b><br/>
<br/>
SSH Server : <input type='checkbox' name='ssh' value='ssh'/>
<br/>
Apache Server : <input type='checkbox' name='web' value='web' />
<br/>
Python2 : <input type='checkbox' name='python' value='python'/>
<br/>
Net-Tools : <input type='checkbox' name='ntool' value='ntool'/>
<br/><br/>
Image Name: <input name="name" /><br/><br/>
<input type='submit' value='Create Image'>
</form>
</center>
""")
