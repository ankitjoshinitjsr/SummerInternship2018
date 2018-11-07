#!/usr/bin/python36
import os
import subprocess
print("content-type: text/html")
print("")

o=subprocess.getoutput("sudo systemctl start shellinaboxd")
print(o)
print("""
<center>
<br>
<br>
<iframe src="http://192.168.43.50:4200" height='300' width='800'></iframe>
<br>
<a href="http://192.168.43.50/homepage.html">Click Here</a> to retrun to home page
</center>
""")

