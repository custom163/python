#!/usr/bin/python
from sys import argv

script, first = argv

txt = open(first)
print " Here is your file: %s" % first
print txt.read()
