#!/usr/bin/python

print("content-type:text/html")
print("")


import socket
import commands as sp
#import subprocess as sp
import cgi
import cgitb
cgitb.enable()

#print("abhishek1")


form=cgi.FieldStorage()
user=form.getvalue('user')
#print(user)



from contextlib import closing

def find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

port=find_free_port()
#print(port)

#print(port)
#fg=str(port)
#print(fg)

x="sudo docker run -dit -p {0}:3333 --name {1}  firefox:v1".format(port,user)
sp.getoutput(x)
#print(a)
#sp.getouput("docker ps ")
print("""
<center>
<a href='http://192.168.43.63:{}'>
<input type='submit' name='firefox' value='launch' width='15'>
</a>
""".format(port))



#print("hello")






