#!/bin/python3
# plus-minus

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    less = 0
    zero = 0
    greater = 0
    tot = len(arr)
    
    if tot == 0:
        return None
    
    for i in arr:
        if i < 0:
            less += 1
        elif i == 0:
            zero += 1
        elif i > 0:
            greater += 1
    
    less = round(less/tot, 6)
    zero = round(zero/tot, 6)
    greater = round(greater/tot, 6)
    
    # Still need to pad if decimals < 6
    print('{:.6f}'.format(greater))
    print('{:.6f}'.format(less))
    print('{:.6f}'.format(zero))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)