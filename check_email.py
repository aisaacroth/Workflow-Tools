#!/usr/bin/env python3
'''
Small script that opens my email clients.

Author: Alexander Roth
Date:   2016-01-17
'''

import sys
import webbrowser

def main():
    webbrowser.open('https://mail.google.com/mail/u/1/#inbox')
    webbrowser.open('https://inbox.google.com/u/0/')


def print_arguments(arg):
    print('python3 {0}'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    else:
        print_arguments(sys.argv[0])
