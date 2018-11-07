#!/usr/bin/python2

print("content-type: text/html")
print("")

import commands as sp
import cgi

form=cgi.FieldStorage()
#print("enter data nodes ip:")
ntt= form.getvalue('ntt')

tt=1
i=1

print("""<b>
<center>
<form action='ans_mr.py' >""")
 
#print("<form> action= 'setup_nn.py' >")
while tt <= int(ntt):	
	print("TASKTRACKERS {} : <input name='sip[0]' /><br/>".format(tt))
	tt+=1	
print("""ENTER USERNAME: <input type='text' name='u' >
<br/>
ENTER JOB TRACKER IP:<input type='text' name='j'>
<br/>
ENTER MASTER IP:<input type='text' name='m'>
<br/>
""")
print("<input type='submit'>")
print("""</form>
</center>
</b>""")
