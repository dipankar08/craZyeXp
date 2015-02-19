#######################
#
#  imaplementaion of my Own Curl 
######################
import urllib
params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
def curlPost(url,data):
  params = urllib.urlencode(data)
  import os
  cmd = 'curl --data "'+params+'" '+url# https://example.com/resource.cgi'
  print cmd
  os.system(cmd)


