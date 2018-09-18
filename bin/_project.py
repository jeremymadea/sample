#!/bin/echo This file is only intended to be imported:
if __name__ == '__main__': raise Exception('File for import only.')

project_name = 'foo'

import sys
from os.path import (normpath, dirname, realpath)
import configparser

basedir = normpath(dirname(realpath(__file__)) + '/..') 
libdir = basedir + '/lib'
etcdir = basedir + '/etc'

# Modify our search path to include ../lib relative to the script's path.
sys.path.append(libdir)
