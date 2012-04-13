import os
from ConfigParser import SafeConfigParser
config = SafeConfigParser()
config.read(os.path.join(os.path.dirname(__file__), 'defaults.cfg'))

def read(var):
    return config.get('data', var)
