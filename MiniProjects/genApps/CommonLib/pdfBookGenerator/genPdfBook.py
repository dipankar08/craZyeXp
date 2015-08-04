import os
import pdb
import random
import string
idx = 0
def getPdfPageFromHtml(html):
  global idx;
  f = open('/tmp/temp'+str(idx)+'.html', 'w')
  f.write(html)
  f.close()
  cmd = 'xvfb-run -a wkhtmltopdf --use-xserver /tmp/temp'+str(idx)+'.html /tmp/temp'+str(idx)+'.pdf'
  os.system(cmd)
  
def getTopicPdf(t):
  global idx;
  wrp = '<div style="border-bottom: 1px solid #6f6632; color: GRAY; font-size: 25px; margin: 0 auto;padding-bottom: 10px; position: relative; text-align: center; text-transform: capitalize; top: 264px; width: 700px;color:#6f6632;">'+t+'</div>'
  getPdfPageFromHtml(wrp)
  x = PdfFileReader(open('/tmp/temp'+str(idx)+'.pdf', 'rb'))
  idx = idx+1;
  return x;

def buildPdfForID(id):
    import os
    try:
        id = str(id)
        cmd = 'xvfb-run -a wkhtmltopdf --use-xserver http://dipankar.ngrok.io/cleancode/'+id+'/look/ /tmp/'+id+'.pdf'
        os.system(cmd)
        return PdfFileReader(open('/tmp/'+str(id)+'.pdf', 'rb'))
    except Exception , e:
      print 'Error at buildPdfForID()',str(e)
      
def savePdf(output,fname):
    outputStream = file(fname, "wb")
    output.write(outputStream)
    outputStream.close()
    print 'Saved!'
from PyPDF2 import PdfFileWriter, PdfFileReader


output = None;
HashQuestionStartLine={}
def buildRecursive(c,pbm): #config and parent book mark
  global output
  global HashQuestionStartLine
  for k,v in c.items():
    inp = getTopicPdf('Chapter:'+k);t=output.getNumPages(); output.addPage(inp.getPage(0));
    bm = output.addBookmark('Chapter:'+k,t , parent=pbm) # add bookmark 
    if isinstance(v, int):
      if not HashQuestionStartLine.get(v):
          inp = buildPdfForID(v);t=output.getNumPages();output.addPage(inp.getPage(0));
          HashQuestionStartLine[v]=t;
      cbm = output.addBookmark('Q #'+str(v),HashQuestionStartLine[v] , parent=bm)  
    if isinstance(v, dict):
       buildRecursive(v,bm);
    if isinstance(v, list):
      for v1 in v:
        if isinstance(v1, int):
          if not HashQuestionStartLine.get(v1):
            inp = buildPdfForID(v1);t=output.getNumPages();output.addPage(inp.getPage(0));
            HashQuestionStartLine[v1]=t;
          cbm = output.addBookmark('Q #'+str(v1),HashQuestionStartLine[v1] , parent=bm)  
        if isinstance(v1, dict):
          buildRecursive(v1,bm);
        
def buildBook(config,fname='output.pdf'):
  global output
  output = PdfFileWriter() # open output
  inp = getTopicPdf('Introduction to problem solving')
  output.addPage(inp.getPage(0))
  p1 = output.addBookmark('Intro', output.getNumPages()-1, parent=None) # add bookmark
  
  inp = getTopicPdf('Preface')  
  t=output.getNumPages(); output.addPage(inp.getPage(0));
  p1 = output.addBookmark('Preface',t , parent=None) # add bookmark  
  
  
  inp = getTopicPdf('Table of content!')  
  t = output.getNumPages();output.addPage(inp.getPage(0));
  p1 = output.addBookmark('TOC',t, parent=None) # add bookmark

  buildRecursive(config,None);  
  
  savePdf(output,fname)
  
def buildBookWrapper(config):   
  rand = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))+'.pdf'
  fname = '/tmp/'+rand
  buildBook(config,fname)
  print 'copying file'
  import shutil
  dst = '/home/dipankar/craZyeXp/MiniProjects/genApps/genApps/StaticFiles/tmp/'
  src = fname
  #pdb.set_trace()
  shutil.copy(src, dst)  
  return rand
   
   
#Sample Testing...
# We shoud have a config is a dict, support int , list and another dict as a value.
# The list can contain otehr in and dict but NOT LIST.
#buildBook({'hello':1,'hello2':[1,2,3],'hello3':{'hello4':[1,2,3]},'hello5':[{'h55':[1,2]},{'h56':[1,2,3]}]})