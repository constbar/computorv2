#!/usr/bin/python3

import os
import sys
import time

import zmq

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from computorv2 import Comp
from termcolor import colored

if __name__ == '__main__':
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print(colored('start testing\n', 'green'))
    while True:
        message = socket.recv()
        print(colored('received expression:', 'green'))
        print(f'{message.decode()}')

        print(colored('program response:', 'green'))
        Comp().default(message.decode())
        print()
        time.sleep(3)
        socket.send(b'')
