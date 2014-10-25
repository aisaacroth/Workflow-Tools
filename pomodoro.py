#!/usr/bin/env python3
''' Simple pomodoro timer, runs on a number of cycles provided by the user.

Author: Alexander Roth
Date:   2014-10-25
'''
import sys
import timer


def main(cycles):
    work_time, rest_time = prepCycle()
    for i in range(0, cycles):
        runCycle(work_time, rest_time)


def prepCycle():
    ''' Prepares cycle time values. Fixed to 25 minutes and 5 minutes.
    '''
    work_time = timer.convertToSeconds(25)
    rest_time = timer.convertToSeconds(5)
    return work_time, rest_time


def runCycle(work_time, rest_time):
    ''' Runs the cycle; sends bell response to terminal and prints out cycle 
    prompts to the user.
    '''
    print("Start of work cycle")
    timer.startTimer(work_time)
    print("\a")
    print("End of work cycle")
    print("Take a short break")
    timer.startTimer(rest_time)
    print("\a")


def print_arguments():
    print('python3 pomodoro.py <number of cycles>')
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(int(sys.argv[1]))
    else:
        print_arguments()
