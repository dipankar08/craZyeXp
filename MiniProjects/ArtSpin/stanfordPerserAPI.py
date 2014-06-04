##############
# API to access :http://nlp.stanford.edu:8080/parser/index.jsp
#
##############
import requests
from bs4 import BeautifulSoup
from nltk.tree import *

def convertStringToTree(a):
  """
  Convert String with Arbitart space and new line , It will retrun perfect Tree for processing nltk.
  """
  a = ' '.join(a.split())
  t = Tree(a)
  print 'Makeing NLTK Tree for :', ' '.join(t.leaves())
  return t
  
def getWebParseTree(s):
  """
  Use Online Access to get parse tree string.
  """
  payload = {'query':s,'parserSelect':'English','parse':'Parse'}
  r = requests.post("http://nlp.stanford.edu:8080/parser/index.jsp", data=payload)
  soup = BeautifulSoup(r.text)
  a = soup.find('pre',{'class':'spacingFree'}).string
  a = ' '.join(a.split())
  t = Tree(a)
  print 'Makeing NLTK Tree for :', ' '.join(t.leaves())
  return t[0] # Me are removing ROOT as it is not required.
#getWebParseTree('')

"""
Example: 
>>> import stanfordPerserAPI
>>> stanfordPerserAPI.getWebParseTree(' I love Python')
u'(ROOT\n  (S\n    (NP (PRP I))\n    (VP (VBP love)\n      (NP (NNP Python)))))'
>>> stanfordPerserAPI.getWebParseTree(' I love Python')
u'(ROOT\n  (S\n    (NP (PRP I))\n    (VP (VBP love)\n      (NP (NNP Python)))))'
>>> print stanfordPerserAPI.getWebParseTree(' I love Python')
(ROOT
  (S
    (NP (PRP I))
    (VP (VBP love)
      (NP (NNP Python)))))
>>> 

"""
