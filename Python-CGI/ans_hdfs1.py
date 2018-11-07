#!/usr/bin/python36

print('content-type: text/html')
print('')

import subprocess
import cgi
import os

form=cgi.FieldStorage()
user=form.getvalue('u')
passw=form.getvalue('p')
ip=form.getvalue('i')
mip=form.getvalue('m')
dr=form.getvalue('d')
node=form.getvalue('n')

print("welcome {}".format(user))

hosts="""[master]
{0}	ansible_ssh_user=root  ansible_ssh_pass=root

[slaves]
{1}	ansible_ssh_user={2}	ansible_ssh_pass={3}
""".format(mip,ip,user,passw)	

subprocess.getoutput("sudo chown apache /etc/ansible/hosts")
fp=open("/etc/ansible/hosts",'w')
fp.write(hosts)
fp.close()

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
       owner: "apache"
       mode: 0755
   - copy:
       dest: "/etc/hadoop/hdfs-site.xml"
       content: "<?xml version=\\"1.0\\"?>\\n<?xml-stylesheet type=\\"text/xsl\\" href=\\"configuration.xsl\\"?>\\n<!-- Put site-specific property overrides in this file. -->\\n<configuration>\\n<property>\\n<name>dfs.name.dir</name>\\n<value>/nn</value>\\n</property>\\n</configuration>\\n"
   - command: "hadoop namenode -format"
   - command: "hadoop-daemon.sh start namenode" 
- hosts: slaves
  tasks:
   - file:
       path: "/{1}"
       state: directory
       owner: "apache"
       mode: 0755
   - copy:
       dest: "/etc/hadoop/hdfs-site.xml"
       content: "<?xml version=\\"1.0\\"?>\\n<?xml-stylesheet type=\\"text/xsl\\" href=\\"configuration.xsl\\"?>\\n<!-- Put site-specific property overrides in this file. -->\\n<configuration>\\n<property>\\n<name>dfs.data.dir</name>\\n<value>/{1}</value>\\n</property>\\n</configuration>\\n"

   - command: "hadoop-daemon.sh start datanode" 
'''.format(mip,dr)

print("playbook written")
subprocess.getoutput("sudo touch /myhadoop/ansible/hdfs_ans.yml")
subprocess.getoutput("sudo chown apache /myhadoop/ansible/hdfs_ans.yml")

f1=open("/myhadoop/ansible/hdfs_ans.yml",'w')
f1.write(ans)
f1.close()

ans=subprocess.getstatusoutput("sudo ansible-playbook /myhadoop/ansible/hdfs_ans.yml ")
print("playbook status={}".format(ans))
jpss=subprocess.getoutput("sshpass -p {} ssh -o StrictHostKeyChecking=no -l root {} jps".format(passw,ip))
jpsm=subprocess.getoutput("sudo jps")
print('<pre>')
print(jpsm)
print(jpss)
print('<pre>')






