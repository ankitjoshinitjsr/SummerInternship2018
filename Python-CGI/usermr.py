#!/usr/bin/python

print("content-type: text/html")
print("")

import cgi
import commands as sp
import cgitb

cgitb.enable()
form=cgi.FieldStorage()
user=form.getvalue('user')
c="""#!/usr/bin/python

import sys
#f=open('/muskan/dataset.csv','r')
dict={}
for i in sys.stdin:
   s=i.split(',')
   key=s[1]
   task=s[7]
   if key in dict:
     if task not in dict[key] and task!='UNKNOWN' and task!='PERMISSION':
        dict[key].append(s[7])
   else:
     dict[key]=[]

#f.close()
"""



sp.getoutput("sudo  touch /map.py")
sp.getoutput("sudo chown apache /map.py")
sp.getoutput("sudo chmod +x /map.py")
fp=open('/map.py','w')
fp.write(c)
fp.close()
fpp=open('/map.py','a')
fpp.write("print(dict['{0}'])".format(user))
fpp.close()


var='''#!/usr/bin/python

import sys

for i in sys.stdin:
'''

sp.getoutput("sudo  touch /red.py")
sp.getoutput("sudo chown apache /red.py")
sp.getoutput("sudo chmod +x /red.py")
fp=open('/red.py','w')
fp.write(var)
fp.close()
fp2=open('/red.py','a')
fp2.write('  '+'print(i)')
fp2.close()

x=sp.getoutput("sshpass -p blackhat scp -o StrictHostKeyChecking=no /map.py /red.py root@192.168.43.85:/muskan/")

y=sp.getoutput('sshpass -p blackhat ssh -o StrictHostKeyChecking=no -l root 192.168.43.85 hadoop jar /usr/share/hadoop/contrib/streaming/hadoop-streaming-1.2.1.jar -input /dataset.csv -mapper /muskan/map.py -file /muskan/map.py -reducer /muskan/red.py -file /muskan/red.py -output /{0}'.format(user))

y=sp.getoutput('sshpass -p blackhat ssh -o stricthostkeychecking=no -l root 192.168.43.85 hadoop fs -cat /{0}/part-00000'.format(user))

x=y.split('.')
z=x[-1].split('[')
print(z[2])


