#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
from os.path import basename
import yaml

from . import config

__author__ = 'Aron Culotta'
__email__ = 'aronwc@gmail.com'
__version__ = '0.1.0'


def get_basenames(files):
    """ Return basename of each file. E.g.:
    >>> get_basenames(['/foo/bar.1.2'])
    ['bar.1']
    """
    return [basename(f)[:basename(f).rfind('.')] for f in files]


def get_files(subdir, extension):
    """ Return all .tags files in the parsed data directory that don't have
    corresponding .scores files. """
    return glob.glob(config.get('data', 'path') + '/' +
                     config.get('data', subdir) + '/*.' + extension)


def parse_twitter_handles():
    yaml_doc = yaml.load(open(config.get('data', 'path') + '/' + config.get('data', 'twitter_yaml'), 'r'))
    return [d for d in yaml_doc if 'twitter' in d['social']]


def parse_legislators():
    yaml_doc = yaml.load(open(config.get('data', 'path') + '/' + config.get('data', 'leg_yaml'), 'r'))
    return [d for d in yaml_doc]
