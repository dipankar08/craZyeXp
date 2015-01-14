code="""
#include<stdio.h>
int main(){
int n,i;
char data[100];
scanf("%d",&n);
printf("%d",n);
for (i = 0;i<n;i++)
  {
    gets(data);
    puts(data);
  }
return 0;
}
"""

input="""
5
dipankar
dipankar123 
"""

import subprocess
import os
class Execute:
  def __init__(self,name='',code='',input='',ftime=None):
    os.system('mkdir ~/tmp')
    if ftime:      
      os.system('wget wget https://gist.githubusercontent.com/netj/526585/raw/9044a9972fd71d215ba034a38174960c1c9079ad/memusg')
      os.system('chmod 777 memusg')
    self.name =name
    self.code =code
    self.input =input
  def save(self,name='hello', code="",input=""):
    code = '#include "common.h"\n' + code
    with open (''+name+'.c', 'w+') as f: f.write (code)
    with open (''+name+'.in', 'w+') as f: f.write (input)
    self.input =input
    
  def compile(self,name='hello'):
    print 'Compiling program ...'
    cmd = "gcc -g  -std=c99 -o %s %s.c" %(name,name)
    print "Launching command: " + cmd  
    sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    out= sp.communicate()
    res={}; res['stdout'] =  out[0]; res['stderr'] =  out[1]
    if 'error:' in res['stderr']:
      res['msg']='syntax Error : Not able to compile'
      res['output'] =res['stderr'];
      res['can_run'] ='no';
    elif 'warning:' in res['stderr']:
      res['msg']='Compiled succesully with warning'
      res['output'] =res['stderr'];
      res['can_run'] ='yes';
    else:
      res['msg']='Compiled succesully.'
      res['output'] =res['msg']
      res['can_run'] ='yes';
    print '*'*50
    print res
    print '*'*50
    return res
    
  def run(self,name=None):
    print '>>> Running program ...'
    cmd = "./%s" %(name)
    print "Launching command: " + cmd  
    sp = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    out= sp.communicate(input=self.input)
    res={}; res['stdout'] =  out[0]; res['stderr'] =  out[1]
    if not res['stderr']:
      res['output'] =res['stdout'];
    else:
      res['output'] = res['stderr']
    print '*'*50
    print res
    print '*'*50
    return res
  def testperf(self,name=None):
    print 'Testing Performance...'
    cmd = "time ./%s" %(name)
    print "Launching command: " + cmd  
    sp = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    out= sp.communicate(input=self.input)
    res={}; res['time'] =  out[1];
    sp.poll()
    
    cmd = "./memusg %s" %(name)
    print "Launching command: " + cmd  
    sp = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    out= sp.communicate(input=self.input)
    res['space'] =  out[1]    
    sp.poll()
    res['output'] = res['time']+res['space']
    
    print '*'*50
    print res
    print '*'*50
    return res

  

