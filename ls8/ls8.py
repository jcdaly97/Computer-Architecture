#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *
print('enter a file name')
filename = str(input())
cpu = CPU()
cpu.load(filename)
cpu.run()
