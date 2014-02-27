################################
# Hi ! This is a lang tut tutorila for learing diffent langugae.
# Uisng common CLI/API, you can learn tutorials easity
# This is kind of cookbook.
# We currently Support following tutorilas.
# 1. Php
# 2. perl
# 3. python
# 4. Rubi
# 5. Java
# 6. C
# 7. C++
#################################

#Common List
SUBJECT =['python','php','perl']
#TOC is the list of dict
TOC=[]
tut ={}

def load_tut():
     pass
def main():
     print '>>> Welcome to Lang tut for easy learing ..'
     # Load tut from disk.
     load_tut()

     sub = raw_input('>>> Please choose the Subject:',str(SUBJECT))
     data = tut.get(sub)
     
     
    
    

