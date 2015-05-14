# this is a automation script for updating values
# use this carefully..
import pdb
def updateSome(dryrun=True):
  from AppsEngines.cleanCode.models import Code
  all = Code.objects.filter()
  nc=0
  ns=0
  com=0;
  pdb.set_trace()
  for c in all:
    #We dont have the code.
	if c.main == None or c.main == '' :
	  c.compilation = 'NO_CODE'
	  nc=nc+1
	elif c.solution == None or c.solution == '' or c.solution == "Explane the code with comaplexity":
	  c.compilation = 'NO_SOLUTION'
	  ns=ns+1
	else:
	  c.compilation = 'COMPLETE'
	  com = com+1
	  print '<',c.id,'>'
	if(not dryrun):
	  c.save()
  print '*'*50
  print 'DRY RUN                         :'+str(dryrun)
  print 'Cont of <no code + No Sol>      :',nc
  print 'Count of <Code + no solution >  :',ns
  print 'Count of <All complete>         :',com
  print '*'*50  
  
updateSome()