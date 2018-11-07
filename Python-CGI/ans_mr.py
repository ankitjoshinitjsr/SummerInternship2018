#!/usr/bin/python2

print('content-type: text/html')
print('')

import cgi
import os
import commands as sp
import cgitb

cgitb.enable()
print('hello')

form=cgi.FieldStorage()
user=form.getvalue('u')
passw=form.getvalue('p')
tracker=form.getvalue('t')
jip=form.getvalue('j')
ip=form.getvalue('i')
mip=form.getvalue('m')

print("<pre>")
print("welcome to trackers page")
sp.getoutput('sudo chown apache /etc/ansible/hosts')
fh=open('/etc/ansible/hosts','w')
print('opened')

jt_ip="""
[jobtracker]
{0}	ansible_ssh_user=root  ansible_ssh_pass=blackhat
[master]
{1}     ansible_ssh_user=root  ansible_ssh_pass=blackhat
""".format(jip,mip)

tt_ip=cgi.FormContent()
fh.write("[tasktrackers]\n")
for i in tt_ip.keys():
	if "sip" in i:
		fh.write(tt_ip[i][0] + "ansible_ssh_user=root   ansible_ssh_pass=blackhat"+"\n")

fh.write(jt_ip)
fh.close()
print('hosts file updated')
print("welcome {}".format(user))

print("\ninventory_overwritten")

ans='''
- hosts: jobtracker,tasktrackers
  tasks:
   - package:
       name: "jdk"
       state: present
   - package:
       name: "hadoop"
       state: present
   - copy:
       dest: "/etc/hadoop/core-site.xml"
       content: "<?xml version=\\"1.0\\"?>\\n<?xml-stylesheet type=\\"text/xsl\\" href=\\"configuration.xsl\\"?>\\n<!-- Put site-specific property overrides in this file. -->\\n<configuration>\\n<property>\\n<name>fs.default.name</name>\\n<value>hdfs://{0}:9001</value>\\n</property>\\n</configuration>\\n"
   
   - copy:
       dest: "/etc/hadoop/mapred-site.xml"
       content: "<?xml version=\\"1.0\\"?>\\n<?xml-stylesheet type=\\"text/xsl\\" href=\\"configuration.xsl\\"?>\\n<!-- Put site-specific property overrides in this file. -->\\n<configuration>\\n<property>\\n<name>mapred.job.tracker</name>\\n<value>{1}:9002</value>\\n</property>\\n</configuration>\\n"

- hosts: jobtracker
  tasks:
   - command: "hadoop-daemon.sh start jobtracker"
     ignore_errors: yes
             
- hosts: tasktrackers
  tasks:
   - command: "hadoop-daemon.sh start tasktracker" 
'''.format(mip,jip)

print("playbook written")
sp.getoutput("sudo touch /myhadoop/ansible/mr_ans.yml")
sp.getoutput("sudo chown apache /myhadoop/ansible/mr_ans.yml")

f1=open("/myhadoop/ansible/mr_ans.yml",'w')
f1.write(ans)
f1.close()

ans=sp.getstatusoutput("sudo ansible-playbook /myhadoop/ansible/mr_ans.yml ")
print("playbook status={}".format(ans))

#starting jobtracker and tasktracker
jpsj=sp.getoutput("sshpass -p root ssh -o StrictHostKeyChecking=no -l root {} jps".format(jip))
#jpst=sp.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} jps".format(passw,ip))

print(jpsj)
#print(jpst)
print("</pre>")






