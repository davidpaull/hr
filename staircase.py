#!/bin/python3
# staircase

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    if n <= 0:
        return False

    nums = []
    for i in range(0, n):
        nums.append(i+1)

    for i in nums:
        i = '#'*i
        print(i.rjust(n, ' '))

if __name__ == '__main__':
    n = int(input())

    staircase(n)