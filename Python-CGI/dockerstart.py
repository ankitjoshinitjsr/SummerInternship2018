#!/usr/bin/python36
print("location: dockerserver.py")
print("content-type: text/html")

import subprocess as sp

sp.getoutput("sudo systemctl restart docker")

print("")
