#!/usr/bin/python36

import subprocess as sp
print("content-type: text/html")
print("")

x=sp.getoutput("sudo hadoop dfsadmin -report")
y=x.split("\n\n")
print(
"""
<table border='1'>
<tr>
<th>Name</th>
<th>Decommission Status</th>
<th>DFS Used</th>
<th>DFS Remaining</th>
<th>DFS Remaining%</th>
</tr>
""")
for a in y[2:]:
     z=a.split('\n')
     if z[0]=='':
        print("</tr>")
        print("<tr>")
     else:
        print("<tr>")
     for b in z:
        v=b.split(':')   
        if v[0]=='Name' or v[0]=='DFS Remaining' or v[0]=='DFS Used' or v[0]=='Decommission Status ' or v[0]=='DFS Remaining%':
           print("<td>"+v[1]+"</td>")
                 
   
print("""
</tr>
</table>
""" 
)
