/******************************************* 

PUZZLE: Conditional break point based on stack infomation

Possible Activation Stacks creted by this program :
1. main ->a->b->c->x           <<<<<<< We Only break on x if it come via b . i.e
2. main ->a ->b ->x            <<<<<<< Break
3. mian ->b->x;                <<<<<<<<<<< Break here;
4  main ->b->c->x                 
3. main ->c->x;
4. main ->x;

Note, Here b () allow braching to x  if i is True  else brach to c

Problem1:
----------
How would you break on x if it come via b , directly or indirectly called.

Gdb Solution :
--------------
gdb hello
break x
disable 1
break b
command 2
silent
enable 1
continue
end

command 1
bt
disable 1
end
r

problem2:
--------------
Put a break point if the following condition got satisfied:
 
1. Stop a, OR
2. stop b iff b is called from a; OR
3. stop x iff x is DIRECTLY/INDIRECTLY called by b and b is called from a 

Solutions:
------------
gdb hello

break a
break b
break x

disable 2
disable 3

command 1
enable 2
bt
c
end

command 2
disable 2
enable 3 if i 
bt
c
end

command 3
disable 3
bt
c
end

r

***************************/

#include<stdio.h>

void a(int i)
{
printf("\nI am in a");
b(i);
}

void b(int i)
{
printf("\nI am in B");
if (i)
  x(i);
else
  c(i);
}

void c(int i)
{
printf("\nI am in C");
x(i);
}

void x(int i)
{
printf("\nI am in X");
}

void main()
{
  int i=0;
  printf("I am in Main");
  /* calling a,b,c,x from main for 3 time each */
  for (i=0;i<2;i++)
  {
    a(i);b(i);c(i);x(i);
  }
}
