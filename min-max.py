#!/bin/python3
# Min-Max Sum

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    min = 0
    max = 0
    
    for i in range(0, len(arr) - 1):
        min += arr[i]
        max += arr[i+1]
        
    print('{} {}'.format(min, max))
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)