#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    left = []
    right = []
    equal = []
    pivot = arr[0]
    for i in arr:
    	if i < pivot:
    		left.append(i)
    	elif i == equal:
    		equal.append(i)
    	else:
    		right.append(i)
    result_list = left + equal + right
    return ' '.join(map(str,result_list))

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    print(result)
