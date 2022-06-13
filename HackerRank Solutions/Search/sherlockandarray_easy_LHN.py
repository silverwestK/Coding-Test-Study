#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    n = len(arr)
    left = 0
    if n > 1:
    	right = sum(arr[1:])
    	for i in range(1,n):
    		if left == right:
    			return 'YES'
    		left = left + int(arr[i-1])
    		right = right - int(arr[i])
    else:
    	return 'YES'
    return 'NO'

if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result)
