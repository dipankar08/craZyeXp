#########################################
#  Version : 1 : Fix 
#
#
##########################################


import sys
import os
import requests
import pdb
print sys.argv
if len(sys.argv) == 1 :
  print 'Enter the start url ...  < Ex: python youtubedl https://www.youtube.com/watch?v=wnoGa83znqw&list=RDtinKQKo4_Nk >'
else:
  print ' Valid Input ... Let me finout all video '

  for ll in sys.argv[1:]:
    r = requests.get('https://www.youtube.com/watch?v=KDckd3G2MzY&list='+str(ll))
    print 'Trying ...',r.text
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.text)
    title = soup.find("h3",  attrs={'class': 'playlist-title'}).text
    print title
    pdb.set_trace()
    s1 = soup.find_all("a",  attrs={'class': 'playlist-video'})
    print len(s1)
    s2 =  [ 'http://www.youtube.com'+i['href'] for i in s1]
    for i in s2:
      print 'Downloaidng .. ',i
      os.system('youtube-dl -o "./Downloads/'+title+'/%(title)s.mp4" '+i)
