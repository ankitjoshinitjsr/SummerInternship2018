#!/usr/bin/python2

print("content-type: text/html")
print("")

import commands as sp
import cgi
import cgitb

cgitb.enable()
form=cgi.FieldStorage()
print(form)
nm=form.getvalue('nn')
ns=form.getvalue('ns')
print(nm,ns)
sj=1
mj=1


print("<form> action='setup_dn.py' </form>")
while sj <=int(ns):
      print("DN {}: <input name='sip[0]' /></br>".format(sj))
      sj+=1


