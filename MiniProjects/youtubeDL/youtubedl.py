import os
import requests
r = requests.get('https://www.youtube.com/watch?v=Lb07fQkZZtc&list=PLD874699E809474DC')
#print r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text)
s1 = soup.find_all("a",  attrs={'class': 'playlist-video'})
print len(s1)
s2 =  [ 'http://www.youtube.com'+i['href'] for i in s1]
for i in s2:
  print 'Downloaidng .. ',i
  os.system('youtube-dl '+i)
