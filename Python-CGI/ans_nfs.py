#!/usr/bin/python36

print('content-type: text/html')
print('')

import subprocess 
import cgi
import os

form=cgi.FieldStorage()
name=form.getvalue('n')
size=form.getvalue('s')
sip=form.getvalue('sv')
cdr=form.getvalue('c')
sdr=form.getvalue('d')
user=form.getvalue('u')
passw=form.getvalue('p')
ip=form.getvalue('i')
print('welcome...{}!!!'.format(user))
#print("\n\n\n{}".format(size))
#entry in hosts file
hosts="""[server]
{0}	ansible_ssh_user=root  ansible_ssh_pass=blackhat

[client]
{1}	ansible_ssh_user=root	ansible_ssh_pass={3}
""".format(sip,ip,user,passw)

#done=os.system("sudo mkdir /myhadoop/ansible")
#print(done)
#k=os.system("sudo touch /myhadoop/ansible/hosts")
#print(k)
x=subprocess.getstatusoutput("sudo chown apache /etc/ansible/hosts")
print(x)
fp=open("/etc/ansible/hosts",'w')
fp.write(hosts)
fp.close()

#print("host file written")
#ansible-playbook for nfs
ans='''
- hosts: all
  tasks:
    - package:
        name: "nfs-utils"
        state: present
    - service:
        name: "nfs"
        state: started
        enabled: yes
- hosts: server
  tasks:
    - lvol:
        vg: vgcloud
        lv: {0}
        size: {1}
        state: present
        force: yes
    - filesystem:
        fstype: ext4
        dev: "/dev/vgcloud/{0}"
    - mount:
        path: /mnt
        src: "/dev/vgcloud/{0}"
        fstype: ext4
        state: mounted
    - file:
        path: "/{2}"
        state: directory 
    - lineinfile:
        path: "/etc/exports"
        line: "/{2}	*(rw,no_root_squash)"
        create: yes
    - service:
        name: "nfs"
        state: restarted
        enabled: yes
- hosts: client
  tasks: 
    - file:
        path: "/{3}"
        state: directory
    - mount:
        path: "/{3}"
        src: "{4}:/{2}"
        fstype: nfs4
        state: mounted
    
'''.format(name,size,sdr,sdr,sip)

subprocess.getoutput("sudo touch /myhadoop/ansible/nfs_ans.yml")
subprocess.getoutput("sudo chown apache /myhadoop/ansible/nfs_ans.yml")
f1=open("/myhadoop/ansible/nfs_ans.yml",'w')
f1.write(ans)
f1.close()

#print("playbook written")

status=subprocess.getstatusoutput("sudo ansible-playbook /myhadoop/ansible/nfs_ans.yml ")
print("<pre>")
print("Successfuly implemented STaaS mounted on {}".format(cdr))
print("</pre>")



