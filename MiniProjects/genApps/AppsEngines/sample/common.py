
import sys, traceback
import os
import pdb

   
def D_LOG():
  
  print '_'*60  
  _, _, tb = sys.exc_info()
  filename, lineno, funname, line = traceback.extract_tb(tb)[-1]
  print "Exception in user code:",filename,':',lineno,')'
  print '-'*60
  os.system('sed -n '+str(lineno-5)+','+str(lineno+5)+'p '+filename)
  print '-'*60
  traceback.print_exc(file=sys.stdout)
  print '_'*60

  
def getCustomException(e,arg=''):
  msg = e.message
  if 'UNIQUE constraint failed' in e.message:
      msg=e.message.replace('UNIQUE constraint failed:','Please ensure following value must be unique:')
  elif 'NOT NULL constraint failed' in e.message:
      msg=e.message.replace('NOT NULL constraint failed:','Please ensure following field MUST have some value:')
  elif 'invalid literal for int() with base 10' in e.message:
      msg=e.message.replace('invalid literal for int() with base 10','Please ensure following value must be a integer:')
      
  #global error on Errro type
  elif isinstance(e,ValueError):
    msg='Type mismatch! You are trying to use wrong data type. Please enter valid '+e.message.split(' ')[0]+'.'
  elif e.__class__.__name__ == 'DoesNotExist':
    msg= 'The '+e.message.split(' ')[0]+' having id <'+str(arg)+'> Does not exist!'

  
  return msg

