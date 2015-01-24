

"Draw a Trangle"
def love(x):
  for i in range(x-1):
     print ' '*(x-i-1),'*'*(i*2+1),' '*(2*(x-i-2)+1),'*'*(i*2+1)
  print ' ', '*'*((x*2-2)*2+1)
  print ' ', '*'*((x*2-2)*2+1)
  for i in range(((x*2-2)*2+1)): 
    print '', ' '*i,'*'*((x*2-2)*2+1-2*i)
love(10)