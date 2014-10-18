#!/usr/bin/env python3
''' A simple script that acts as a timer for a given number of minutes.
Sends a call to the os to make a bell call when complete.

Author: Alexander Roth
Date: 2014-10-18
'''
import sys
import time


def main(arg_list):
    minutes = getMinutes(arg_list)
    seconds = convertToSeconds(minutes)
    startTimer(seconds)
    print("\a")


def getMinutes(arg_list):
    return int(arg_list[1])


def convertToSeconds(minutes):
    return minutes * 60


def startTimer(seconds):
    time.sleep(seconds)

def print_arguments():
    print("python3 timer.py <minutes>")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments()
