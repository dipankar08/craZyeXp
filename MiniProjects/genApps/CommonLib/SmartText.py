############# This Smart Text to HTml ##################
#
# Standardization
#  1. Starting with # is p1
#  2. Staring with  * is p2
#  3. {{{  Code }}}
#  4. {{  input box }}
#  5. starting with -  is ul li
#  6. Staring with -- nested ul li
#  7. Starting with 1. ol li
#  8. Single line Break : new para
#  9. Double line Break : New section
#  10. ** bold ** inside line indicate bold
#  11. ***  italic ***
#  12. {{{MAIN_CODE}}} Replace by it's own code.
#  13 ------------------- Line is a section
#
# Not supported:
# http://stackoverflow.com/editing-help
########################################################
import pdb
import re
def smartTextToHtml(txt,extra):
  "Smart text"
  #1. Do a replacement text by extra.
  for k,v in extra.items():
    if v:
      txt = txt.replace(k,v)
  #2. Split by new line.
  txt = txt.split('\n')
  #3. Remove leading spaces unless it is under {{ }} or {{{  }}}
  is_rem_spc = True
  #pdb.set_trace()
  for i in range(len(txt)):
    if(is_rem_spc):
      txt[i] = txt[i].strip()
    if( '{{{' in txt[i] or '{{' in txt[i] ):
      is_rem_spc = False
    print i
    if((i+1) < len(txt) and ('}}}' in txt[i+1] or '}}' in txt[i+1])):
      is_rem_spc = True 
  
  #4. Analizing and outputting.
  fInsideLI= False
  fInsideOL = False
  fInSideSection = False
  fInsideCode = False
  for i in range(len(txt)):
    now = txt[i]    
    #1. ** Hello ** -> <b>hello</b>
    if(now.startswith('***') and now.endswith('***')): now = '<u><b><i>'+now[3:-3] +'</i></b></u>'
    #1. ** Hello ** -> <b>hello</b>
    if(now.startswith('**') and now.endswith('**')): now = '<b>'+now[2:-2] +'</b>'
    #1. * Hello * -> <i>hello</i>
    if(now.startswith('*') and now.endswith('*')): now = '<i>'+now[1:-1] +'</i>'

    #Handling LI and UL
    if(now.startswith('-')):
      if fInsideLI:
        now = '<li>'+now[1:]+'</li>'
      else:
        now = '<ul><li>'+now[1:]+'</li>'
        fInsideLI = True
      if(i+1< len(txt) and not txt[i+1].startswith('-')):
        fInsideLI = False
        now += '</ul>'
    #Handling LI and OL
    if( re.match('^[0-9]+\.', now) ):
      if fInsideOL:
        now = '<li>'+now[now.find('.')+1:]+'</li>'
      else:
        now = '<ol><li>'+ now[now.find('.')+1:] +'</li>'
        fInsideOL = True
      if(i+1< len(txt) and not re.match('^[0-9]+\.', txt[i+1]) ):
        fInsideOL = False
        now += '</ol>'
    
    #Handling {{ }} and {{{ -- do --}}}
    if('{{' in now or '{{{' in now):
      fInsideCode = True
    if('}}' in now or '}}}' in now):
      fInsideCode = False
    
    now = now.replace('{{{','<pre class="code"><code class="language-clike ">')
    now = now.replace('}}}','</code></pre>')
    now = now.replace('{{','<pre class="code">')
    now = now.replace('}}','</pre>')
    
    
    #Handaling section like  ==== and ----
    if(i+1 < len(txt) and txt[i+1].startswith('----')):
        now = '<h2>'+now+'</h2>'
        txt[i+1] ='NOP' # Next line is no operation
    elif(i+1 < len(txt) and txt[i+1].startswith('====')):  
        now = '<h1>'+now+'</h1>'
        txt[i+1] ='NOP'
    elif now != '' and now != 'NOP' and not fInSideSection: #It's not an empty line.
        now = '<h3>'+now
        fInSideSection = True;
    #Empty Line Specify a New Section as h3
    if now =='' and fInSideSection and not fInsideCode:
       now = '</h3>'
       fInSideSection = False
    
    #if previous line is ended with HTML text, we shoud put a BR for new  line ?
    if(i-1 >=0 and not txt[i-1].endswith('>') and txt[i-1] != 'NOP'):
      now = '<br>' + now
    
    #Assign Back
    txt[i] = now
    
    
  #end of for
  if fInSideSection:
     txt.append('</h3>')
     fInSideSection = False 
       
  #5. Joining back and returned.
  ret = '\n'.join([ t  for t in txt if t != 'NOP'])
  print ret
  return ret
  








