#############################
# Spped up by dipankar
#
##############################
from log import D_LOG
import pdb
from threading import Thread
import threading
class Worker(Thread):   
    ans =[]
    def __init__(self, id,target, **args):
        self.id = id
        #self.ans = None
        self._target = target
        self._args = args
        super(Worker, self).__init__()
        self.ans = None
    def run(self):
        try:
            self.ans = self._target(**self._args)
            if self.ans:#Add ans only if it is not None
              Worker.ans.append(self.ans)
        except Exception,e :
            print 'error',e
            D_LOG()
#Public Funcs are here..

def speedUp(func,data_queue,max_t_count =5 ):
  print '>>> Initilize speedUp ...... '
  MAX_THREAD_COUNT = max_t_count
  tcount =0
  threads = []
  AS = [] 
  Worker.ans =[]
  while not data_queue.empty():
    if threading.activeCount() <= MAX_THREAD_COUNT:
      tcount = tcount+1
      t = Worker(tcount,func,**data_queue.get())
      threads.append(t)
      t.start()
  # synchronize all threads
  for t in threads:
    t.join()
  print '>>> complete speedUp ...... '
  return Worker.ans
  
########## Test case ###########

#1. Define a function Here..
import time
def func(i,j):
  print '[func] doing squr',j,i
  time.sleep(1);
  return i

#2. Define a Data Set having dict as taken by func
import Queue
QQ = Queue.Queue()
for i in range(20):
  QQ.put({'i':i,'j':i+5})

#3. Fire Up the Operation.
if 0:
  print speedUp(func,QQ,15);
