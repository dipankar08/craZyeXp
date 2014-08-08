'''
Created on Aug 2, 2014

@author: Dipankar
'''
class CodeGenerator:
    def __init__(self, indentation=' '*2):
        self.indentation = indentation
        self.level = 0
        self.code = ''

    def indent(self):
        self.level += 1

    def dedent(self):
        if self.level > 0:
            self.level -= 1

    def __add__(self, value):
        temp = CodeGenerator(indentation=self.indentation)
        temp.level = self.level
        now_str = ''
        for x in str(value).split('\n'):
            if (len(x) != 0):
                now_str = now_str + self.indentation * self.level + x.strip() +'\n'
        temp.code = self.code+now_str
        return temp
    def __mul__(self, value):
        " Here Mult used for add Will Preserve the Indentation "
        temp = CodeGenerator(indentation=self.indentation)
        temp.level = self.level
        now_str = ''
        for x in str(value).split('\n'):
            now_str = now_str + self.indentation * self.level + x +'\n'
        temp.code = self.code+now_str
        return temp
    def sp(self):
        "insert space"
        self.code += "\n"

    def __str__(self):
        return str(self.code)

############ test code ##############
if 0:
    a = CodeGenerator()
    a += """
    aaaa
    bbbb
    cccc
    """
    a += 'for a in range(1, 3):\n'
    a.indent()
    a += 'for b in range(4, 6):\n'
    a.indent()
    a += 'print(a * b)\n'
    a.dedent()
    a += '# pointless comment\n'
    a += """
    I am  bad boy
    I love football"""
    a*="""
1
 2
  3"""
    print a


###########################################