from subprocess import *
import subprocess
import sys
from subprocess import PIPE, Popen
from threading  import Thread
import time
try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty  # python 3.x

ON_POSIX = 'posix' in sys.builtin_module_names

#######3  Helpers ######################
#Enque Data
def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()
#Comand Input
def receive(q):
  cmd = ['break main','run','quit']
  for c in cmd:
    time.sleep(5)
    q.put(c+'\n')
    

class pyGdb:
  def __init__(self,file_name):
    self.file_name = file_name
    self.rerun()
    
  def rerun(self):
    self.p = Popen(['gdb', self.file_name], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,bufsize=1, close_fds=ON_POSIX)
    
    self.q_stdout = Queue()
    t = Thread(target=enqueue_output, args=(self.p.stdout, self.q_stdout))
    t.daemon = True # thread dies with the program
    t.start()


    self.q_stdin = Queue()
    t1 = Thread(target=receive, args=(self.q_stdin,))
    t1.daemon = True # thread dies with the program
    t1.start()
  
  def getOutput(self):
    data=''
    while(True):
      try:  
        #line = q.get_nowait()
        line = self.q_stdout.get(timeout=1)
      except Empty:
          if self.p.poll() != None:
            print 'Bebug Completed'
          break
          #x= q1.get()
          #print '(gdb)', x
          #p.stdin.write(x)
      else: # got line
          data+= line.replace('(gdb)','')
    return data          
    
  def start(self):
    print 'Starting gdb...'
    data = self.issueCmd('run')
    #time.sleep(5); # Wait for start..
    return data
    
  def issueCmd(self,cmd):
    cmd+='\n'
    data=''
    data+='(gdb) '+ cmd
    self.p.stdin.write(cmd)
    data+=self.getOutput()
    return data
  def is_running(self):
    if self.p.poll() != None:
      print 'Bebug Completed'
      return True
    else:
      return False
  

#gdb = pyGdb('./sum.exe');
#print gdb.startGdb()
#print gdb.issueCmd('break main')




# feed your commands here...
#p.stdin.write('\n')


