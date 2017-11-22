#!/usr/local/bin/python3

'''
Write a threaded program emulating grep -n that uses one thread to search in each filename passed. Regex can be included or ignored as you see fit.
'''

import sys, os
import threading


class Worker(threading.Thread):
    def run(self):
        local = threading.local()
        # path and file handle should be isolated from other thread
        local.path = path
        with open(local.path,'r', errors='ignore') as local.infile:
            count_line = 1
            for line in local.infile.read().splitlines():
                if keyword in line:
                    # it looks complicated here, but all I want is printing out everything in different colors
                    print('\033[1;35m%s\033[1;m\033[1;32m:%s:\033[1;m' % (local.path, count_line),
                            line.replace(keyword, '\033[1;31m'+keyword+'\033[1;m'))
                count_line += 1

def grep(args):
    global path,keyword
    if len(args) < 3:
        sys.exit('USAGE:   python3 NameofPythonFile.py keyword path[ path...]\nEXAMPLE: python3 A.py keyword *')
    keyword = args[1]
    for path in args[2:]:
        if not os.access(path, os.R_OK):
            print('ERROR: ', path, ': Permission denied')
        elif os.path.isdir(path):
            print('ERROR: ', path, ': Is a directory')
        else:
            w = Worker(args=(path, keyword))
            w.start()



if __name__ == '__main__':
    grep(sys.argv)
