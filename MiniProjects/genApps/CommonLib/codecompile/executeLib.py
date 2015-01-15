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
import pdb
class Execute:
  def __init__(self,lang="c",name='',code='',input='',ftime=None):
    os.system('mkdir ~/tmp')
    if ftime:      
      os.system('wget wget https://gist.githubusercontent.com/netj/526585/raw/9044a9972fd71d215ba034a38174960c1c9079ad/memusg')
      os.system('chmod 777 memusg')
    self.name =name
    self.code =code
    self.input =input
    self.lang=lang;
    #Decide
    if self.lang =='py':
      self.prog_file_name=''+name+'.py'
      self.input_file_name=''+name+'.in'
      self.prog_obj_name=''+name+'.py'
    else:
      self.prog_file_name=''+name+'.c'
      self.input_file_name=''+name+'.in'
      self.prog_obj_name=''+name+'.exe'
      
  def save(self,name='hello', code="",input=""):
    #Code Inject
    if self.lang =='c':
      code = '#include "common.h"\n' + code
    
    with open (self.prog_file_name, 'w+') as f: f.write (code)
    with open (self.input_file_name, 'w+') as f: f.write (input)
    self.input =input
    
  def compile(self,name='hello'):
    print 'Compiling program ...'
    #decide
    if self.lang =='py':      
      cmd = "pylint %s" %(self.prog_file_name)
    else:          
      cmd = "gcc -g  -std=c99 -o %s %s" %(self.prog_obj_name,self.prog_file_name)
    
    
    print "Launching command: " + cmd  
    sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    out= sp.communicate()
    res={}; res['stdout'] =  out[0]; res['stderr'] =  out[1]
    
    #3. Analize Result
    if self.lang =='py':
      if 'E:' in res['stdout']:
        res['msg']='syntax Error : Not able to compile'
        res['output'] =res['stdout'];
        res['can_run'] ='no';
      elif 'W:' in res['stdout']:
        res['msg']='Compiled succesully with warning'
        res['output'] =res['stdout'];
        res['can_run'] ='yes';
      else:
        res['msg']='Compiled succesully.'
        res['output'] =res['msg']
        res['can_run'] ='yes';
    else: # for c Code..
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
    #pdb.set_trace()
    #decide
    if self.lang =='py':
      cmd = "python ./%s" %(self.prog_obj_name)
    else:    
      cmd = "./%s" %(self.prog_obj_name)
    print '>>> Running program ...'
    
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
    #TODO for python 
    print 'Testing Performance...'
    cmd = "time ./%s.exe" %(name)
    print "Launching command: " + cmd  
    sp = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    out= sp.communicate(input=self.input)
    res={}; res['time'] =  out[1];
    sp.poll()
    
    cmd = "./memusg %s.exe" %(name)
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

  

