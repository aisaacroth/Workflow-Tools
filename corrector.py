#!/usr/bin/env python3
'''
Author: Alex Roth
Date:   2015-02-15
'''
import re
import sys

THE_W_REGEX = re.compile('^teh$')

def main():
    pass

def print_arguments():
    print('python3 {0} <filename>'.format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        print_arguments()
