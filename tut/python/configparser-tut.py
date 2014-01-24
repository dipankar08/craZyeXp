#1 Create a config File
>>> import ConfigParser
>>> config = ConfigParser.RawConfigParser()
>>> config.add_section('Section1')
>>> config.set('Section1', 'an_int', '15')
>>> config.set('Section1', 'a_bool', 'true')
>>> config.set('Section1', 'a_float', '3.1415')
>>> config.set('Section1', 'baz', 'fun')
>>> 
>>> with open('config-tut.cfg', 'wb') as configfile:
...   config.write(configfile)
... 
>>> del config

# Read a config file
>>> config = ConfigParser.RawConfigParser()
>>> config.read('config-tut.cfg')
['config-tut.cfg']
>>> x = config.getint('Section1', 'an_int') # Return Integer
>>> x
15
>>> 15 +4
19
>>> x = config.get('Section1', 'an_int') # Retrun sring only
>>> x
'15'
>>> print config.items('Section1')
[('an_int', '15'), ('a_bool', 'true'), ('a_float', '3.1415'), ('baz', 'fun')]
>>> 

# Update any Config or delete config.
>>> config.set('Section1','an_int',100) #update
>>> print config.items('Section1')
[('an_int', 100), ('a_bool', 'true'), ('a_float', '3.1415'), ('baz', 'fun')]
>>> config.remove_option('Section1','an_int') # remove
True
>>> print config.items('Section1')
[('a_bool', 'true'), ('a_float', '3.1415'), ('baz', 'fun')]
>>> print config.sections() # list sections
['Section1']
>>> 


