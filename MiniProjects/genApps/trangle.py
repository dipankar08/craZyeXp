

"Draw a Trangle"
def trangle(x):
  for i in range(x/2+1):
    print ' '*(x/2-i),
    print '*'*(2*i+1);

trangle(20)