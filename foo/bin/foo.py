#!/usr/bin/env python 
from _project import *

import foolib


print(libdir)
config = configparser.ConfigParser()
config.read(etcdir + '/' + project_name + '.ini')

print(config['default']['foo'])
print('"{}"'.format(eval(config['default']['bar'])))
