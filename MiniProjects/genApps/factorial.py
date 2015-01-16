

def fact(i):
  if(i==0):
    return 1;
  else:
    return i*fact(i-1)

print fact(3)