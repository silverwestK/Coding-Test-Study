#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1,n):
    	tmp_i = i
    	for j in range(i-1, -1, -1):
    		if arr[j] > arr[tmp_i]:
    			tmp_j = arr[j]
    			arr[j] = arr[tmp_i]
    			arr[tmp_i] = tmp_j
    			tmp_i -= 1
    	print(' '.join(map(str,arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
