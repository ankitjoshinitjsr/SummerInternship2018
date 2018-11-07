#!/usr/bin/python2

print("content-type: text/html")
print("")

import commands as sp
import cgi
import cgitb
cgitb.enable()

form=cgi.FieldStorage()
#print("enter data nodes ip:")
ns= form.getvalue('ns')

sj=1
i=0

print("""<b>
<center>
<form action='ans_hdfs2.py' >""")
 
#print("<form> action= 'setup_nn.py' >")
while sj <= int(ns):	
	print("DN {0} : <input name='sip[{1}]' /><br/>".format(sj,i))
	sj+=1	
        i+=1
print("""ENTER USERNAME: <input type='text' name='u' >
<br/>
ENTER DIRECTORY: <input type='text' name='d'>
<br/>
ENTER MASTER IP:<input type='text' name='m'>
<br/>
""")
print("<input type='submit'>")
print("""</form>
</center>
</b>""")
