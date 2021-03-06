#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import ConfigParser
import os
import sys

__author__ = 'Aron Culotta'
__email__ = 'aronwc@gmail.com'
__version__ = '0.1.4'

config = ConfigParser.RawConfigParser()
if 'PURPLE_CFG' in os.environ:
    config.read(os.environ['PURPLE_CFG'])
else:
    from os.path import expanduser
    home = expanduser("~")
    config.read(home + os.path.sep + '.purpletag')


sys.stdout = codecs.getwriter('utf8')(sys.stdout)

# make directories
path = config.get('data', 'path')
for subdir in 'jsons', 'tags', 'scores', 'web':
    try:
        os.makedirs(path + '/' + config.get('data', subdir))
    except:
        pass
