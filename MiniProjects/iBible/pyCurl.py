#######################
#
#  imaplementaion of my Own Curl 
######################
import urllib
params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
def curlPost(url,data):
  params = urllib.urlencode(data)
  import os
  cmd = 'curl --data "'+params+'" '+url# https://example.com/resource.cgi'
  print cmd
  os.system(cmd)

f = open('toc.txt')
a = f.read()
b = a.split('\n')
topic= None 
for i in b:
  if i.startswith('T.'):
    topic = i.replace('T.','').strip()
  elif i.startswith('Q.'):
    qline = i.replace('Q.','').strip()
    name = qline[:qline.find('#')].strip()
    short_desc = qline[qline.find('#')+1:].strip()
    curlPost('http://192.168.56.101:7777/api/code/',{'name':name,'short_desc':short_desc,'full_desc':'More about the question like sample Q and Ans ..','intro':'Write Basic Intro ex: Baic way to solve the problem or approach and Algorithm of the below code','solution':'Explane the code with comaplexity','topic':topic})
  else:
   print '>>>>> Error at line:',i

