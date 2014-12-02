
import sys, traceback
import os
import pdb

   
def D_LOG():
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
  #pdb.set_trace()

