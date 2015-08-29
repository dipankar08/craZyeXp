###########################################################
#  This is Stubs : App dev shroud fill it with logic      #
#                                                         #
###########################################################

def authenticate(func):
  " This is a decorator to do the authetication logic "
  def inner(*args, **kwargs): 
    print "Arguments were: %s, %s" % (args, kwargs)
    ###############################################
    
    #  WRITE YOUR AUTH LOGIC HERE                 #
    
    ###############################################
    return func(*args, **kwargs) 
  return inner
