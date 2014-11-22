######################
# Effictence call Stack if there are any runtime error inside try cat block
#######################
import traceback
import sys
import os
def D_LOG(flag = 0):
  import pdb  
  print '_'*60  
  _, _, tb = sys.exc_info()
  filename, lineno, funname, line = traceback.extract_tb(tb)[-1]
  print "Exception in user code:",filename,':',lineno,')'
  print '-'*60
  os.system('sed -n '+str(lineno-5)+','+str(lineno+5)+'p '+filename)
  print '-'*60
  traceback.print_exc(file=sys.stdout)
  print '_'*60
  if flag != 0:
    pdb.set_trace()



#example
if 0:
  try:
     a ='aaa'/12
  except:
     print 'this is a error'
     D_LOG(1)

  print 'done !'
