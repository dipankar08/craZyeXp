import os
import ConfigParser
def get_common_config():
  from os.path import expanduser
  ROOT_PATH = expanduser("~")
  CONTACT_FILE_LOC =os.path.join(ROOT_PATH,".contacts.pkl")
  CONFIG_FILE_LOC =os.path.join(ROOT_PATH,".config.ini")
  config = ConfigParser.ConfigParser()
  config.read(CONFIG_FILE_LOC)
  return config 

c = get_common_config();
