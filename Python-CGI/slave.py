#!/usr/bin/python36
print("content-type: text/html")
print("")

import os
import subprocess
import cgi

data=cgi.FieldStorage()
Dir=data.getvalue('dir')
Ip=data.getvalue('sip')
masterIp=data.getvalue('mip')
Pass=data.getvalue('pass')
print(Dir,Ip,masterIp,Pass)
s=subprocess.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} rpm -q jdk1.8".format(Pass,Ip))
print(s)
#Installing JDK1.8
if s[0]!=0:
   x=subprocess.getoutput("sshpass -p {0} scp -o StrictHostKeyChecking=no /jdk-8u171-linux-x64.rpm root@{1}:/".format(Pass,Ip))
   print(x)
   x=subprocess.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} rpm -ivh /jdk-8u171-linux-x64.rpm".format(Pass,Ip))
   print(x)
#Creating a .bashrc file for slave system
   x="""# .bashrc

# User specific aliases and functions
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi
iptables -F
setenforce 0
export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/
export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH
"""
   subprocess.getoutput("sudo chown apache /hadoop/.bashrc")
   f=open('/hadoop/.bashrc','w')
   f.write(x)
   f.close()
   subprocess.getoutput("sshpass -p {0} scp -o StrictHostKeyChecking=no /hadoop/.bashrc root@{1}:/root/.bashrc".format(Pass,Ip))
   x=subprocess.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} java -version".format(Pass,Ip))
#hadoop Setup   
x=subprocess.getoutput("sshpass -p {0} scp -o StrictHostKeyChecking=no /hadoop-1.2.1-1.x86_64.rpm root@{1}:/".format(Pass,Ip))
x=subprocess.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1}  rpm -ivh /hadoop-1.2.1-1.x86_64.rpm --force".format(Pass,Ip))

#hdfs-site.xml for slave
x="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{0}</value>
</property>
</configuration>
""".format(Dir)
os.system("sudo chown apache /hadoop/hdfs-site.xml")
f=open('/hadoop/hdfs-site.xml','w')
f.write(x)
f.close()

#core-site.xml for slave
x="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{0}:9001</value>
</property>
</configuration>
""".format(masterIp)
os.system("sudo chown apache /hadoop/core-site.xml")
f=open('/hadoop/core-site.xml','w')
f.write(x)
f.close()

os.system("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} mkdir /{2}".format(Pass,Ip,Dir))

x=subprocess.getoutput("sshpass -p {0} scp -o StrictHostKeyChecking=no /hadoop/hdfs-site.xml root@{1}:/etc/hadoop/".format(Pass,Ip))
x=subprocess.getoutput("sshpass -p {0} scp -o StrictHostKeyChecking=no /hadoop/core-site.xml root@{1}:/etc/hadoop/".format(Pass,Ip))

#Starting Slave Daemon Process
x=subprocess.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} hadoop-daemon.sh start datanode".format(Pass,Ip))


x=subprocess.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} jps | grep DataNode".format(Pass,Ip))
print(x)

