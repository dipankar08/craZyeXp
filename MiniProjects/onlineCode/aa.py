import os.path, subprocess
from subprocess import STDOUT, PIPE
def compile_stat():
  pass
def run_stat():
  pass
def compile_code (code_file,prog='java',inp=''):
    if prog == 'java':
       cmd=['javac', code_file+'.java']
    if prog =='c':
       cmd=['gcc', code_file+'.c']
    if prog == 'c++':
       cmd=['g++', code_file+'.cpp']
    #subprocess.check_call(cmd)
    proc =subprocess.Popen(cmd, stdout = PIPE, stderr = PIPE,stdin=PIPE)
    ans ={}
    ans['ERROR'] = proc.stderr.read()
    ans['OUTPUT'] = proc.stdout.read()
    return ans

def execute_code (code_file,prog='java',inp=''):
    if prog == 'java':
       cmd=['java', code_file]
    if prog =='c':
       cmd=['./a.out']
    if prog == 'c++':
       cmd=['./a.out']

    proc =subprocess.Popen(cmd, stdout = PIPE, stderr = PIPE,stdin=PIPE)
    proc.stdin.write(inp)
    proc.stdin.close()
    ans ={}
    ans['ERROR'] = proc.stderr.read()
    ans['OUTPUT'] = proc.stdout.read()
    return ans
        
#print compile_code("test",'c++')
#print execute_code("test",'c++','1000')


print compile_code("test",'c')
print execute_code("test",'c','1000\n2000')
