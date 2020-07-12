#!/usr/bin/python -tt

import sys
import os
import re

# Define a main() function that prints a little greeting.

vidext = '.avi'
subext = '.srt'
    
def listpath(dir):
  a = os.listdir(dir)
  print a
  sub = {}
  vid = {}
  for path in a:
    path = os.path.join(dir,path)
    print path
    if os.path.isfile(path) :
      match = re.search(r'(.*\\)(.*)(\.\w+)$',path)
      if match:
        if subext in match.group(3):
          epi = re.search('.*(\d\d)',match.group(2))
          sub[epi.group(1)] = path
        elif vidext in match.group(3):
          epi = re.search('.*(\d\d)',match.group(2))
          vid[epi.group(1)] = path
  for epino in sub.keys() :
    path = sub[epino]
    newn = vid[epino][:-len(vidext)] + subext
    print 'Original :', path
    print 'New      :', newn
    os.rename(path,newn)
    print '...'



# Define a main() function that prints a little greeting.
def main():
  a = listpath(sys.argv[1])
      
  

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
