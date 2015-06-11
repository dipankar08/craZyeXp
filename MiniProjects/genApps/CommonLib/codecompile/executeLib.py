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
import time
import fcntl, os

BASE_PATH = '/tmp/'
OK = 1
ERROR = 0

### My SubProcess  With TimeOut with default time out is 15 sec.
def  TimeOutByPolling(p,timeout=15): 
  # poll for terminated status till timeout is reached
  # Return True if timeout occure..
  t_beginning = time.time()
  seconds_passed = 0
  while True:
      if p.poll() is not None:
          break
      seconds_passed = time.time() - t_beginning
      if timeout and seconds_passed > timeout:
          p.terminate()
          return True;
      time.sleep(0.1)
  return False
def normFileName(sentence):
  import re
  sentence = re.sub('[^A-Za-z0-9]+', '', sentence)
  return sentence
def GCC_FORMETTED_ERROR(a):
  #pdb.set_trace()
  try:
    a1 =  [ x.split(':') for x in a.split('\n') if ('warning' in x)] #waring then Error
    a2 = [ x.split(':') for x in a.split('\n') if ('error' in x)]
    a=a1+a2
    # filter valid data
    a =  [x for x in a if x[1].isdigit()]
    # Modify common error message
    for i in a:
       j = i[4]
       if j.find('(') != -1: j = j[:j.find('(')]
       if j.find('{') != -1: j = j[:j.find('{')]
       if j.find('[') != -1: j = j[:j.find('[')]
       i[4] = j
    return a;
  except Exception , e:
    print 'Error: Not able to generated formated Error',e
    return []

import urllib
def NameURLLocalPath(jar):
  res =[]
  jars = [ j.strip() for j in jar.split(',') if j ]
  for j in jars:
    fname = j[j.rfind('/')+1:]
    fname_mod = fname.replace('.zip','') # Name shoud not include .zip like abc.jar.zip => abc.jar
    res.append((fname_mod,j,BASE_PATH+fname))
  return res
  
def DownloadAndResolveJar(jars):
  " We willd ownlad the jar in /tmp/ and put it dr."
  try:
    NUP = NameURLLocalPath(jars) # << <name, url,path >>
    alreay_have = os.listdir(BASE_PATH)
    succ_list=[]
    k = None
    for j in NUP:
      if j[0] not in alreay_have:
        print '>>> Downloading jar/zip ... ', j
        k =j
        testfile = urllib.URLopener()
        testfile.retrieve(j[1], j[2])
        if(j[2].endswith('.zip')):
          print 'Unzipping ',j[2],'....'
          os.system('unzip '+j[2]+' -d /tmp/')
      else:
        print '\n[INFO] Skipping Download for Jar file as already exist',j[0]

        
    # Let Recheck and Very fy...
    for j in NUP:
      if j[0] in alreay_have:
        succ_list.append(j[0])
    return ( OK, 'Successfully Ported:\n...'+ '\n...'.join(succ_list))
  except Exception ,e :
    return ( ERROR, 'Not able to resove dependency\n...For File:'+str(k)+'\n...Due to:'+str(e))  

   
class Execute:
  def __init__(self,lang="c",name='',main='',func='',input='',depends='',ftime=None):
    os.system('mkdir ~/tmp')
    if ftime:      
      os.system('wget wget https://gist.githubusercontent.com/netj/526585/raw/9044a9972fd71d215ba034a38174960c1c9079ad/memusg')
      os.system('chmod 777 memusg')
    #Normalized name a single string.. as you know that..
    name = normFileName(name)
    print 'We are usng file name as:<%s> ' %name 
    self.name = name
    self.main = main
    self.func = func
    self.input =input+'\n'
    self.lang=lang;
    self.depends = depends;
    #Decide
    if self.lang =='py':
      self.prog_file_name  = BASE_PATH +name+'.py'
      self.func_file_name  = BASE_PATH +name+'_func.py'
      self.input_file_name = BASE_PATH +name+'.in'
      self.prog_obj_name   = BASE_PATH +name+'.py'
      self.compile_cmd  = "pylint %s" %(self.prog_file_name)
      self.run_cmd  = "python %s" %(self.prog_obj_name)
    elif self.lang =='cpp':
      self.prog_file_name= BASE_PATH +name+'.cpp'
      self.func_file_name  = BASE_PATH +name+'_func.cpp'
      self.input_file_name= BASE_PATH +name+'.in'
      self.prog_obj_name= BASE_PATH +name+'.exe'
      self.compile_cmd  = "g++  -std=c++11 -g -o %s %s" %(self.prog_obj_name,self.prog_file_name)
      self.run_cmd  = "%s" %(self.prog_obj_name)
    elif self.lang =='java':
      self.prog_file_name= BASE_PATH +name+'.java'
      self.func_file_name  = BASE_PATH +name+'_func.java'
      self.input_file_name= BASE_PATH +name+'.in'
      self.prog_obj_name=  name
      if not self.depends:
        self.compile_cmd  = "javac -d %s %s" %(BASE_PATH,self.prog_file_name)
        self.run_cmd  = "java -classpath %s %s" %(BASE_PATH, self.prog_obj_name)
      else:
        dps = ':'.join([ BASE_PATH+a[0] for a in NameURLLocalPath(self.depends) ])
        self.compile_cmd  = "javac -cp \"%s\" -d %s %s" %(dps, BASE_PATH, self.prog_file_name)        
        self.run_cmd  = "java -cp \"%s:%s\" %s" %(BASE_PATH, dps,  self.prog_obj_name)
      
    
    else:
      self.prog_file_name=BASE_PATH+name+'.c'
      self.func_file_name  = BASE_PATH +name+'_func.c'
      self.input_file_name= BASE_PATH+name+'.in'
      self.prog_obj_name= BASE_PATH+name+'.exe'
      self.compile_cmd  = "gcc -g  -std=c99 -o %s %s" %(self.prog_obj_name,self.prog_file_name)
      self.run_cmd  = "%s" %(self.prog_obj_name)
  def ResolveDependency(self): 
    " Resolve dependency .."
    if self.lang =='java':
      r = DownloadAndResolveJar(self.depends)
    return r
      
  def save(self,name='hello', main="",func ='', input=""):
    #Code Inject
    #pdb.set_trace()
    if self.lang =='c':
      #TBD: code = '#include "common.h"\n' + code
      main = '#include "'+self.name+'_func.c'+'" \n' + main
    elif self.lang =='cpp':
      main = '#include "'+self.name+'_func.cpp'+'" \n' + main
    elif self.lang =='java':
      pass
    elif self.lang =='py':
      main = 'import '+self.name+'_func \n' + main
    else: # dor c
      main = '#include "'+self.name+'_func.c'+'" \n' + main
    #pdb.set_trace()  
    with open (self.prog_file_name, 'w+') as f: f.write (main)
    with open (self.func_file_name, 'w+') as f: f.write (func)
    with open (self.input_file_name, 'w+') as f: f.write (input)
    self.input =input+'\n'
    
  def compile(self,name='hello'):
    print 'Compiling cmd:',self.compile_cmd
    #pdb.set_trace()
    res={}; 
    #Decide if some depency to be solved before compile the app.
    if self.depends:
      ret = self.ResolveDependency()
      if ret[0] == ERROR:
        res['can_run'] ='no'
        res['output'] = ret[1] + '\n'
        return res;
      else:
        res['output'] = ret[1] + '\n'
    else:
      res['output'] =''
 
    sp = subprocess.Popen(self.compile_cmd , shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    #Compilation Is alwas finite time - no need to add timeout.
    out= sp.communicate()   
    res['stdout'] =  out[0]; res['stderr'] =  out[1]
    #pdb.set_trace()
    #3. Analize Result
    if self.lang =='py':
      if 'E:' in res['stdout']:
        res['msg']='syntax Error : Not able to compile'
        res['output'] += res['stdout'];
        res['can_run'] ='no';
      elif 'W:' in res['stdout']:
        res['msg']='Compiled succesully with warning'
        #res['output'] +=res['stdout']; # No need to show lot of gurbae for python 
        res['can_run'] ='yes';
      else:
        res['msg']='Compiled succesully.'
        res['output'] += res['msg']
        res['can_run'] ='yes';
    else: # for c,c++,java Code..
      res['formated_error'] = GCC_FORMETTED_ERROR(res['stderr'])
      if 'error:' in res['stderr']:
        res['msg']='Syntax Error : Not able to compile\n'
        res['output'] += res['msg']+res['stderr'];        
        res['can_run'] ='no';
      elif 'warning:' in res['stderr']:
        res['msg']='Compiled succesully with warning\n'
        res['output'] += res['msg'] + res['stderr'];
        res['can_run'] ='yes';
      else:
        res['msg']='Compiled succesully.'
        res['output'] += res['msg']
        res['can_run'] ='yes';
    print '*'*50
    print res
    print '*'*50
    return res
    
  def run(self,name=None):
    #pdb.set_trace()
    res={};    
    print "Launching command: " + self.run_cmd  
    sp = subprocess.Popen(self.run_cmd , shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    fcntl.fcntl(sp.stdout.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)
    fcntl.fcntl(sp.stderr.fileno(), fcntl.F_SETFL, os.O_NONBLOCK)
    print '>>>>> Running ith Input:<',self.input,'>'
    sp.stdin.flush()
    sp.stdin.write(self.input)
    sp.stdin.flush()
    #out= sp.communicate(input=self.input)
    
    if TimeOutByPolling(sp):
       res['stdout'] =  ''; res['stderr'] =  ''
       res['msg'] = 'TimeOut: review your code :\n Q1. is your program contins a infinite loop?\n Q2  did you provide all the  necessary inputs ?\n Q3. is your program can run in 5 sec ?\n '
       res['can_run'] ='no';
       res['output'] = res['msg']
       return res;
    
    try:
      res['stdout'] = sp.stdout.read()
      res['stderr'] = sp.stderr.read()
    except:
      print 'Errr: Not able to read'    
    
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

  

