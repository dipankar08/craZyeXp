#############################
# Spped up by dipankar
#i Addon Read from Generator Insted of Queue..
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

def speedUp(func,gen,max_t_count =5 ):
  print '>>> Initilize speedUp ...... '
  MAX_THREAD_COUNT = max_t_count
  tcount =0
  AS = [] 
  Worker.ans =[]
  if gen: # in case the generator is null
    while True:
        try:
            data = gen.next()
            while(threading.activeCount() == MAX_THREAD_COUNT):
               pass
            tcount = tcount+1
            t = Worker(tcount,func,**data)
            t.start()
        except StopIteration:
            print 'gen end..'
            break;
        except Exception,e :
            print 'error',e
            D_LOG()
  
  # ignoring logic to sync of all thread  we are checking some sometime for anotherc thread..
  flag =1
  while(threading.activeCount() > 1):
    print '[main thread] Now Thread count',threading.activeCount();
    if flag ==1:
      time.sleep(60); # ping time..
    if (threading.activeCount() == 1 ):
       flag =0
       time.sleep(30) # wat time// hope we will have more thread at that time.. :)
    else:
       flag = 1

    if(flag ==0):
      break;
  print '>>> complete speedUp ...... '
  return Worker.ans
  
########## Test case ###########

#1. Define a function Here..
import time
def func(i):
  print '[func] doing squr',i
  time.sleep(5);
  return i

#2. Define a Data Set having dict as taken by func
def simple_generator_function():
  for i in range(10):
    yield {'i':i}

gen = simple_generator_function()

#3. Fire Up the Operation.
if 0:
  print speedUp(func,gen,3);
