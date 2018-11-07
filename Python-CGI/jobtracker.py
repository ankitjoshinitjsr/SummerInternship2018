#!/usr/bin/python36
print("content-type: text/html")
print("")

import os
import subprocess 
import cgi,cgitb

cgitb.enable()
print("hello")
data=cgi.FieldStorage()
Ip=data.getvalue('jtip')
Pass=data.getvalue('pass')
print(Ip+Pass)

print("<pre>")
s=subprocess.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} rpm -q jdk1.8".format(Pass,Ip))
#Installing JDK1.8
if s[0]!=0:
   x=subprocess.getoutput("sshpass -p {0} scp -o StrictHostKeyChecking=no /jdk-8u171-linux-x64.rpm root@{1}:/".format(Pass,Ip))
   x=subprocess.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} rpm -ivh /jdk-8u171-linux-x64.rpm".format(Pass,Ip))
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
export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/
export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH
iptables -F
setenforce 0
"""
   subprocess.getoutput("sudo chown apache /hadoop/.bashrc")
   f=open('/hadoop/.bashrc','w')
   f.write(x)
   f.close()
   subprocess.getoutput("sshpass -p {0} scp -o StrictHostKeyChecking=no /hadoop/.bashrc root@{1}:/root/.bashrc".format(Pass,Ip))
   x=subprocess.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} java -version".format(Pass,Ip))

x=subprocess.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1}  rpm -ivh /hadoop-1.2.1-1.x86_64.rpm --force".format(Pass,Ip))
print(x)

x="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>
</configuration>
""".format(Ip)

x=subprocess.getoutput("sudo chmod 777 /hadoop/mapred-site.xml")
print(x)
x=subprocess.getoutput("sudo chown apache /hadoop/mapred-site.xml")
print(x)
f=open('/hadoop/mapred-site.xml','w')
f.write(x)
f.close()

x="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{0}:9001</value>
</property>
</configuration>
""".format(Ip)
os.system("sudo chown apache /hadoop/core-site.xml")
os.system("sudo chmod 777 /hadoop/mapred-site.xml")
f=open('/hadoop/core-site.xml','w')
f.write(x)
f.close()

x=subprocess.getoutput("sshpass -p {0} scp -o StrictHostKeyChecking=no /hadoop/mapred-site.xml root@{1}:/etc/hadoop/".format(Pass,Ip))
x=subprocess.getoutput("sshpass -p {0} scp -o StrictHostKeyChecking=no /hadoop/core-site.xml root@{1}:/etc/hadoop/".format(Pass,Ip))

x=subprocess.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} hadoop-daemon.sh start jobtracker".format(Pass,Ip))
print(x)

x=subprocess.getoutput("sshpass -p {0} ssh -o StrictHostKeyChecking=no -l root {1} jps | grep JobTracker".format(Pass,Ip))
print(x)
print("</pre>")

