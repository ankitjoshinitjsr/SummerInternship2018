#!/usr/bin/python36

print('content-type: text/html')
print('')

import subprocess 
import cgi
import os

form=cgi.FieldStorage()
name=form.getvalue('n')
size=form.getvalue('s')

ans='''
- hosts: server
  tasks:
    - lvol:

'''
