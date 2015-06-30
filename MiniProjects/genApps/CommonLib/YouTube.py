#Youtube related API
# using http://np1.github.io/pafy/
import pafy
def getID(a):
  if a.rfind('v=') != -1:
    s = a.rfind('?v=')+3
    t = a[s:]
    u = t.rfind('&')
    if u != -1:
      return t[:u]
    return t
  else:
    return None
def getYoutubeData(url,more=True,audio=True,isPlayList=False):
  if not isPlayList:
    return getYoutubeVideo(url,more,audio)
  else:
    return getYoutubePlayList(url,more,audio)
    
def getYoutubeVideo(url,more=True,audio=True):
  res={}
  res['type'] = 'VIDEO'
  if url == None:
      return {'status':'error','res':None,'msg':'URL should be look like: https://www.youtube.com/watch?v=bMt47wvK6u0'}
  id = getID(url)
  if id == None:
     id = url
     
  url = 'https://www.youtube.com/watch?v='+url
  try:
      video = pafy.new(url)
      res['thumb']=video.thumb
      res['title'] = video.title
      res['rating'] = video.rating
      res['length'] = video.length
      res['rating'] = video.rating
      res['duration'] = video.duration
      res['description'] = video.description[:100]+'...'
      best = video.getbest()
      res['bestUrl'] = best.url
      res['bestResolution'] = best.resolution
      res['bestExtension'] = best.extension
      res['otherurls'] = []
      if more:
        streams = video.streams
        for s in streams:
          now={}
          now['resolution'] = s.resolution
          now['extension'] = s.extension
          now['filesize'] = "{0:.2f}".format(s.get_filesize()/(1024*1024.0))+'MB'
          now['url'] = s.url
          res['otherurls'].append(now)
          
      res['audiourls'] = []
      if more:
        streams = video.audiostreams
        for s in streams:
          now={}
          now['bitrate'] = s.bitrate
          now['extension'] = s.extension
          now['filesize'] = "{0:.2f}".format(s.get_filesize()/(1024*1024.0))+'MB'
          now['url'] = s.url
          res['audiourls'].append(now)
      return {'status':'success','res':res,'msg':'data returned'} 
  except Exception,e:
      return {'status':'error','res':None,'msg':'Unknown Error'+str(e)} 

      
def getYoutubePlayList(url,more=False,audio=False):
    res = {}
    res['type'] = 'LIST'
    try:
        import pafy
        playlist = pafy.get_playlist(url)       
        res['title'] = playlist['title']
        res['author'] = playlist['author']
        res['description'] = playlist['description']
        res['count'] = len(playlist['items'])
        res['list'] =[]
        for p in playlist['items']:
          now={}
          x = p['pafy']
          now['title']=  x.title
          now['thumb']= x.thumb
          now['length']= x.length
          now['duration']= x.duration
          if more:
            now['extension']= x.getbest().extension
            now['filesize'] = "{0:.2f}".format(x.getbest().get_filesize() /(1024*1024.0))+'MB'
            now['url'] = x.getbest().url
          res['list'].append(now)
        return {'status':'success','res':res,'msg':'data returned'} 
    except Exception ,e:
      return {'status':'error','res':None,'msg':'Unknown Error'+str(e)}
#print getYoutubeData('https://www.youtube.com/watch?v=u5sd1YeI9ok')