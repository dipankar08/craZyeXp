
import sys, traceback
def D_LOG():
  print '-'*60
  print "Exception in user code:"
  traceback.print_exc(file=sys.stdout)
  print '-'*60
  import pdb
  pdb.set_trace()

