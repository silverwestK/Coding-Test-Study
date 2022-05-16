#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort(key=int)
    n = len(arr)
    mins = 10000000
    d_list = []
    for i in range(n):
    	if i+1 < n:
    		if arr[i+1] - arr[i] == mins:
    			d_list.append(arr[i])
    			d_list.append(arr[i+1])
    		elif arr[i+1] - arr[i] < mins:
    			mins = arr[i+1] - arr[i]
    			d_list = []
    			d_list.append(arr[i])
    			d_list.append(arr[i+1])
    		else:
    			continue
    return d_list



if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(result)
