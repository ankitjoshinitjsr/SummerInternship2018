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
ip=form.getvalue('i')
mip=form.getvalue('m')
dr=form.getvalue('d')
print(user)
print("<pre>")
print("welcome {}".format(user))

print("welcome to hosts page")
sp.getoutput('sudo chown apache /etc/ansible/hosts')
fh=open('/etc/ansible/hosts','w')
print('opened')

master_ip="""[master]
{0}	ansible_ssh_user=root  ansible_ssh_pass=blackhat

""".format(mip)	

slave_ip=cgi.FormContent()
fh.write("[slaves]\n")

for i in slave_ip.keys():
         if "sip" in i:
		fh.write(slave_ip[i][0] + " ansible_ssh_user=root   ansible_ssh_pass=blackhat"+"\n")

fh.write(master_ip)
fh.close()
print('hosts file updated')

print("\ninventory_overwritten")

ans='''
- hosts: all
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
                
- hosts: master
  tasks:
   - file:
       path: "/nn"
       state: directory
      
   - copy:
       dest: "/etc/hadoop/hdfs-site.xml"
       content: "<?xml version=\\"1.0\\"?>\\n<?xml-stylesheet type=\\"text/xsl\\" href=\\"configuration.xsl\\"?>\\n<!-- Put site-specific property overrides in this file. -->\\n<configuration>\\n<property>\\n<name>dfs.name.dir</name>\\n<value>/nn</value>\\n</property>\\n</configuration>\\n"
   - command: "echo Y | hadoop namenode -format"
   - command: "hadoop-daemon.sh start namenode" 
- hosts: slaves
  tasks:
   - file:
       path: "/{1}"
       state: directory
   - copy:
       dest: "/etc/hadoop/hdfs-site.xml"
       content: "<?xml version=\\"1.0\\"?>\\n<?xml-stylesheet type=\\"text/xsl\\" href=\\"configuration.xsl\\"?>\\n<!-- Put site-specific property overrides in this file. -->\\n<configuration>\\n<property>\\n<name>dfs.data.dir</name>\\n<value>/{1}</value>\\n</property>\\n</configuration>\\n"

   - command: "hadoop-daemon.sh start datanode" 
   - command: "hadoop-daemon.sh start datanode" 
   - command: "hadoop-daemon.sh start datanode" 
   - command: "hadoop-daemon.sh start datanode" 
'''.format(mip,dr)

print("playbook written")
sp.getoutput("sudo touch /myhadoop/ansible/hdfs_ans.yml")
sp.getoutput("sudo chown apache /myhadoop/ansible/hdfs_ans.yml")

f1=open("/myhadoop/ansible/hdfs_ans.yml",'w')
f1.write(ans)
f1.close()

ans=sp.getstatusoutput("sudo ansible-playbook /myhadoop/ansible/hdfs_ans.yml ")
print("</pre>")

print("playbook status={}".format(ans))
#jpss=sp.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} jps".format(passw,ip))
print('<pre>')
jpsm=sp.getoutput("sudo jps")
print(jpsm)
#print(jpss)
print('</pre>')






