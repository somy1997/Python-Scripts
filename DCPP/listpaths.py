#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import os
import re

def listpath(dir):
  a = os.listdir(dir)
  for path in a:
    path = os.path.join(dir,path)
    if os.path.isfile(path) :
      print path
    elif os.path.isdir(path) :
      print path
      listpath(path)



# Define a main() function that prints a little greeting.
def main():
  a = listpath(sys.argv[1])


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
