#!/usr/bin/python2
import commands
import cgi
import cgitb

cgitb.enable()
print "content-type: text/html" 
print
print "<center>"
print("<iframe name='i1' height='300' width='800'></iframe>")
print "<h1>Manage The Containers</h1>"
print "<br/><hr/><br/>"
print""" 
<script>
function lw(mycname)
{
document.location='dockerremove.py?x='+mycname;

}
function lw2(mycname2)
{
document.location='dockerstop.py?y='+mycname2;

}
function lw3(mycname3)
{
document.location='docker_start.py?z='+mycname3;

}
</script>
"""

print "<table border='5'>"
print "<tr><th>Image Name</th><th>Container Name</th><th>IP Address</th><th>Status</th><th>Stop</th><th>Start</th><th>Remove</th><th>console</th></tr>"
#Display all running Containers
z=1
for i in commands.getoutput("sudo docker ps -a").split('\n'):
    if z == 1:
       z+=1
       pass
    else:
       j=i.split()
       cStatus=commands.getoutput("sudo docker inspect {0} | jq '.[].State.Status'".format(j[-1]))
#Display All Ipaddress of container
       ipstatus=commands.getstatusoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(j[-1]))
       portnumber=commands.getstatusoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Ports'".format(j[-1]))
       portnumber=portnumber[1].strip()
       x=portnumber.split(':')
       x=x[-1].split('}')
       portnumber=x[0].split('"')
       try:
         print("<tr><td> " + j[1] + "' </td><td> " + j[-1] + " </td><td>" + ipstatus[1].strip('"') + "</td><td>" + cStatus + "</td><td> <input value='" +j[-1]+"' type='button' onclick=lw2(this.value) /> </td><td> <input value='" +j[-1]+"' type='button' onclick=lw3(this.value) /> </td><td> <input value='" + j[-1] + "' type='button' onclick=lw(this.value) /> </td>"+"<td><a href='http://192.168.43.50:{0}' target='i1'><input type='submit' value='start'></a></td></tr>".format(portnumber[1]))
       except:
         x="It's Fine"

print "</table>"
print "</center>"
