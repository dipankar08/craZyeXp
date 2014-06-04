#############################################
# # Will do kind of tree menupulation of the Grammer Tree
# Author : dipankar
#
#############################################
import stanfordPerserAPI
from nltk.tree import *

class Node(object):
    def __init__(self, pos,text='',children=None):
        self.pos = pos
        self.text = text
        self.parent = None
        if children:
          self.children = children
        else:
          self.children =  []

    def add_child(self, obj):
        self.children.append(obj)
    def getPOS(self):
      return self.pos
    def getText(self):
      return self.text
    def isLeaf(self):
      return self.children ==  []
    def __repr__(self):
      return '<'+self.pos+','+self.text+'>'
    def __str__(self):
      return '<'+self.pos+','+self.text+'>'

#############test code
#n1 =Node('s','abc')
#n1.getPOS()
#n1.getText()

#n2 =Node('t','xyz')
#print n2.getPOS()
#print n2.getText()

#n1.add_child(n2)
#print n1.isLeaf()
#print n2.isLeaf()
       
class Sentences(object):
  """
  This is a Tree Like Grammar tree but we can realize tree based on it's grammar
  # Thsi Will CReate a Parent Pointer TRee
  """
  def __init__(self,t):
    """
    It will create Tree from Stanford Tree
    """
    if not isinstance(t[0],Tree):
      #Leaves
      self.root = Node(t.node,t[0])
    else:
      #Internal Node
      self.root =Node(t.node)
      for c in t:
        newC = self.makeTree(c)
        self.root.add_child(newC)
        newC.parent = self.root
    
  
  def makeTree(self,t):
    """
    It will create Tree from NLTK Tree : Works
    """
    if not isinstance(t[0],Tree):
      #Leaves
      return Node(t.node,t[0])
    else:
      #Internal Node
      n =Node(t.node)
      for c in t:
        newC = self.makeTree(c)
        n.add_child(newC)
        newC.parent = n
      return n

  def printf(self,temp = None):
    """
    Works.
    print Inorder traversal of the tree, It will print the main sentences.
    """
    if temp == None : #beg
       return '\n '+self.printf(self.root)
    else:
       if temp.isLeaf():
         return ' '+temp.text+' '
       else:
         sol=""
         for x in temp.children:
           sol += self.printf(x)
         return sol
           
  def printTree(self,temp = None,depth=0):
    """
    Works
    print Tree in Tree Structure
    """
    if temp == None : #beg 
       return self.printTree(self.root)
    else:
       if temp.isLeaf():
         return '  '*depth+'TreeLeaf('+temp.pos+','+temp.text+')\n'
       else:
         sol=""
         sol+= '  '*depth+'TreeNode('+temp.pos+',\n'
         for x in temp.children:
           sol+= self.printTree(x,depth+1)
         print '\b \b'
         sol+= ')'
         return sol
    def __str__(self):
      self.printTree()
    def __repr__(self):
      self.printTree()

  def getPOSsubTree(self,pos,start = None):
    """
    Works
    Return root of sub Tree having specify POS
    # Do In Order Search and Return Indipended and overlapping Tree
    #Working
    """
    SubTreeList =[]
    if start == None : #beg
        return self.getPOSsubTree(pos,self.root)
    else:
       if start.pos == pos:
         return [ start]
       else:
         for x in start.children:
           SubTreeList += self.getPOSsubTree(pos,x)
       return SubTreeList

  def splitComplexSentence(self,POS=None):
    """
    Works
    For a Complex Sentence it will return as [ Main Sentence without clause, clasue1, clause2 ... ]
    """
    clss = s.getPOSsubTree('SBAR')
    for cls in clss:
      if cls:
        cls.parent.children.remove(cls) # Removeing clause from sentenses
    return [s.root]+clss

    
  def TreetoList(root=None):
    """
    Return Subject Verb and Object of a simple sentences.
    Input: a Tree of simple Sentences.
    """
    result =[]
    if root == None : #beg
        return self.TreetoList(self.root)
    else:
    
    
    
    
    
    








       
  def getPOSlistsubTree(self,poslist,start = None):
    """
    Return root of sub Tree having specify POS
    # Do In Order Search and Return Indipended and overlapping Tree
    """
    SubTreeList =[]
    if start == None : #beg
        return self.getPOSlistsubTree(poslist,self.root)
    else:
       if start.pos == pos[0]:
         return [ start]
       else:
         for x in start.children:
           SubTreeList += self.getPOSlistsubTree(pos,x)
       return SubTreeList       
       

    
  def splitCompundSentence(self,POS=None):
    """
    For a Complex Sentence it will return as [ Main Sentence without clause, clasue1, clause2 ... ]
    #Not Works
    """
    clss = s.getPOSsubTree('SBAR')
    for cls in clss:
      if cls:
        cls.parent.children.remove(cls) # Removeing clause from sentenses
    return [s.root]+clss
    

    
  def returnTriplet(root=None):
    """
    Return Subject Verb and Object of a simple sentences.
    Input: a Tree of simple Sentences.
    """
    result =[]
    if root == None : #beg
        return self.returnTriplet(self.root)
    else:
          
    


    
  def isSimpleSentence():
    """
    Return True if it a simple Sentences.
    """
    pass
  def isComplexSentence():
    """
    Return True if it a Complex Sentences.
    """
    pass
  def isCompoundSentence():
    """
    Return True if it a Compound Sentences.
    """
    pass    
  def isComplexCompoundSentence():
    """
    Return True if it a Complex Counund Sentences.
    """
    pass    
  def getSubVerbPredicate():
    """
    Return Subject Verb and predicate.
    """
    pass   
  def getCaluseList():
    """
    Return List of Clause part and How it is Attached with main subjectsf
    """
    pass 
    

  
  def getSentenceVariation():
    """
    Will Return list of modified subject, with different Clause positions 
    """
    pass 
    

    
## test
x = stanfordPerserAPI.getWebParseTree('The park is so wonderful when the sun is setting and a cool breeze is blowing')
#print x
s =Sentences(x)
#print '\n\n Print Tree:',s.printf()
print s.printTree()
#print s.getPOSsubTree('SBAR')
(a,b) = s.splitComplexSentence()
print a,b
print s.printf(a)
print s.printf(b)

