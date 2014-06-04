#######################
# Simple Spinner Class to do Spin a TEXT by replacing a word.
# Objcetive : 
#
#
########################

import re
import random
from nltk.corpus import wordnet
from nltk.tokenize import regexp_tokenize
import nltk.data
from nltk.stem.porter import *


class ProcessText:
  @staticmethod
  def splitToSentences( content):
    """
    split a paragraph into sentences.
    - you can use the following replace and split functions or the nltk sentence tokenizer
    - content = content.replace("\n", ". ") and return content.split(". ")    
    """
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    return tokenizer.tokenize(content)


class SpinHelper:
  @staticmethod
  def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

  @staticmethod
  def getSynonyms(word,type=None):
      """
      - get all synonyms of a word from the wordnet database it also include the original word
      - Return as  synonyms = [word]
      """
      synonyms = []
      s = None
      if type:
        s = wordnet.synsets(word,pos= SpinHelper.get_wordnet_pos(type))
      else:
        s = wordnet.synsets(word)
        return []
      for syn in s:
        for lemma in syn.lemmas:
          if lemma.name != word:
            w, n = re.subn("_", " ", lemma.name)
            synonyms.append(w)
      s = list(set(synonyms))
      return len(s), s
   
  @staticmethod
  def spin( s):
    """
    function to spin spintax text using regex
    Input :"{Spinning|Re-writing|Rotating|Content spinning|Rewriting} is {fun|enjoyable|entertaining|exciting|enjoyment}! try it {for yourself|on your own|yourself|by yourself|for you} and {see how|observe how|observe} it {works|functions|operates|performs|is effective}."
    Output : Any Spin Text
    """
    while True:
        s, n = re.subn('{([^{}]*)}',
                    lambda m: random.choice(m.group(1).split("|")),
                    s)
        if n == 0: break
    return s.strip()
    
  @staticmethod
  def normSentence():    
    import os, sys
    from subprocess import Popen, PIPE
    import nltk

    BP = os.path.dirname(os.path.abspath(__file__))
    CP = "%(BP)s/opennlp-tools-1.4.3.jar:%(BP)s/opennlp-tools-1.4.3/lib/maxent-2.5.2.jar:%(BP)s/opennlp-tools-1.4.3/lib/jwnl-1.3.3.jar:%(BP)s/opennlp-tools-1.4.3/lib/trove.jar" % dict(BP=BP)
    print CP
    cmd = "java -cp %(CP)s -Xmx1024m opennlp.tools.lang.english.TreebankParser -k 1 -d %(BP)s/opennlp.models/english/parser" % dict(CP=CP, BP=BP)
    print cmd
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
    stdin, stdout, stderr = (p.stdin, p.stdout, p.stderr)
    text = "This is my sample sentence."
    stdin.write('%s\n' % text)
    ret = stdout.readline()
    print 'cccc',ret
    ret = ret.split(' ')
    #prob = float(ret[1])
    tree = nltk.Tree.parse(' '.join(ret[2:]))
      


###############################
#Main Algorithms is here
#     Transform text into spintax with the folowing steps
#     1. split the text to sentences
#     2. loop through the sentences and tokenize it
#     3. loop through each token, find its stem and assemble all the synonyms of it into the spintax
###############################     
class Spinner:
    def getSpinTax(self, text):
        """
        - It generate Spin TAX - Synxtztz
        """
        sentences = ProcessText.splitToSentences(text)
        stemmer = PorterStemmer()
        spintax = ""
        for sentence in sentences:
            #tokens = regexp_tokenize(sentence, "[\w']+")
            tokens = nltk.word_tokenize(sentence)
            tagged_token = nltk.pos_tag(tokens)
            for token,pos in tagged_token:
                n, syn = SpinHelper.getSynonyms(token,pos)
                if n != 0:
                  spintax += "{"
                  for x in range(n):
                    spintax += syn[x]
                    if x != n-1:
                      spintax += "|"
                  spintax += "} "
        return spintax

    def UniqueSpinText(self, spin_tax):
      """
      - It will return only One Random Text.
      - 
      """
      return SpinHelper.spin(spin_tax)



if __name__ == '__main__':
    SpinHelper.normSentence()
    s = Spinner()
    spintax = s.getSpinTax('Many people must live and die alone, even dipankar')
    spun = s.UniqueSpinText(spintax)
    print spintax
    print spun
