#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    n = len(arr)
    for i in range(n//2):
    	arr[i][1] = '-'
    arr.sort(key = lambda x : int(x[0]))
    s_list = []
    for i in arr:
    	s_list.append(i[1])
    print(' '.join(s_list))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
