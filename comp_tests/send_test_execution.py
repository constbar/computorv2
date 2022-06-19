#!/usr/bin/python3

import sys
from random import randint

import zmq
from termcolor import colored

import complex_nums_tests
import functions_tests
import matrices_tests
import rationals_syntax_tests


def help_func():
    print('for all tests, run the program without arguments')
    print('for specific cases, enter the name of the test')
    print('options:')
    print('matrices_tests', 'functions_tests', sep='\n')
    print('complex_nums_tests', 'rationals_syntax_tests', sep='\n')
    sys.exit()


if __name__ == '__main__':
    if len(sys.argv) > 2:
        help_func()
    elif len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']:
        help_func()
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'matrices_tests':
            tests = matrices_tests.matrices_tests
        elif sys.argv[1] == 'functions_tests':
            tests = functions_tests.functions_tests
        elif sys.argv[1] == 'complex_nums_tests':
            tests = complex_nums_tests.complex_nums_tests
        elif sys.argv[1] == 'rationals_syntax_tests':
            tests = rationals_syntax_tests.rationals_tests
        else:
            print('unknown test name')
            sys.exit()
    else:
        tests = matrices_tests.matrices_tests +  \
            functions_tests.functions_tests + \
            complex_nums_tests.complex_nums_tests + \
            rationals_syntax_tests.rationals_tests

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    print(colored('start submitting tests', 'green'))
    print()

    for _ in tests:
        r = randint(0, len(tests) - 1)
        if '=' in tests[r]:
            socket.send(tests[r].encode())
        else:
            socket.send(f'exp = {tests[r]}'.encode())
        message = socket.recv()
        print('sent:', colored(tests[r], 'green'))
