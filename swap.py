#!/usr/bin/python
import sys
#lists = []
array = []
with open('/home/kiran/pyswap/file') as f:
    content = f.read().splitlines()
    print content
    wordCount = len(content)
    print wordCount
    temp = content[0]
    content[0] = content[wordCount-1]
    content[wordCount-1] = temp
    print content

