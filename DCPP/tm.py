#!/usr/bin/python -tt

import sys
import os
import re

# Define a main() function that prints a little greeting.

'''
For windows, use \ as path separator and tm = '[<name>\x99]'
'''
tm = '[<name>™]'


def newname(path, type):
    if type == 1:
        match = re.search(r'(.*)(\[.+\])(\.\w+)$', path)
        if match:
            if tm in match.group(2):
                return ''
            if not re.search(r'\d', match.group(2)):
                newn = match.group(1) + tm + match.group(3)
                return newn
        match = re.search(r'(.*\/)(.*)(\.\w+)$', path)
        if match:
            if '.' in match.group(2) and ' ' not in match.group(2):
                newn = match.group(1) + match.group(2) + '.' + tm + match.group(3)
                return newn
            elif ' ' in match.group(2):
                newn = match.group(1) + match.group(2) + ' ' + tm + match.group(3)
                return newn
            else:
                newn = match.group(1) + match.group(2) + tm + match.group(3)
                return newn
        return path
    elif type == 2:
        match = re.search(r'(.*)(\[.+\])$', path)
        if match:
            if tm in match.group(2):
                return ''
            if not re.search(r'\d', match.group(2)):
                newn = match.group(1) + tm
                return newn
        match = re.search(r'.*\/(.*)$', path)
        if not match:
            return path
        if '.' in match.group(1) and ' ' not in match.group(1):
            newn = path + '.' + tm
        elif ' ' in match.group(1):
            newn = path + ' ' + tm
        else:
            newn = path + tm
        return newn


def listpath(dir):          # DFS order of execution
    a = os.listdir(dir)     # list the files in the directory
    for path in a:          # for each path in a
        path = os.path.join(dir, path)  # resolve path
        if os.path.isfile(path):        # if file
            newn = newname(path, 1)     # its a file, call new name with type = 1
            print('Original :', path)   # original path
            print('New      :', newn)   # new path
            if not newn == '':
                os.rename(path, newn)   # rename only if new path is not null
            print('...')
        elif os.path.isdir(path):       # if dir
            newn = newname(path, 2)     # its a dir, call new name with type = 2
            print('Original :', path)   # original path
            print('New      :', newn)   # new path
            if not newn == '':          
                os.rename(path, newn)   # rename only if not null
                print('...')            
                listpath(newn)          # repeat process with this dir
            else:
                print('...')
                listpath(path)          # repeat process with this dir


# Define a main() function that prints a little greeting.
def main():
    listpath(sys.argv[1])


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
