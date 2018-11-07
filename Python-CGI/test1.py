f=open('/filter.csv','r')
x=''
for i in f:
    i=i.strip()
    x=x+i+'\n'
f.close()

dict={   "NETWORKFILESYSTEM":101,"DOCKER":102,"HADOOPHDFS":103,"HADOOPMAPREDUCE":104,"PERMISSION":105,"nfs": "12","hdfs": "13","mapreduce": "14", "namenode": "1", "jobtracker": "2", "container": "3","docker": "103","/etc/exports": "5","hdfs-site": "6","core-site": "7","Dockerfile": "8","mapred-site": "9","mapred": "10","core": "11",'chown': "15","chmod": "16", "UNKNOWN": "0"}

list=['chown','chmod','namenode','jobtracker','container','/etc/exports','hdfs-site','core-site','Dockerfile','mapred-site','mapred','core','nfs','hdfs','docker','mapreduce']

y=x.split('\n')

for i in y:
     try:
      s1=i.split(',')
      for j in list:
          if j in s1[1] or j in s1[3] or j in s1[4]:
             f=open('/newdata.csv','a')
             f.write(dict[j]+','+dict[s1[6]]+'\n')
             f.close()
             break
     except:
         print("missing")

