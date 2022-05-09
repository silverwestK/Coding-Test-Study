#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    c_n = arr[-1]
    for i in range(n-2, -1, -1):
    	if(arr[i] > c_n):
    		arr[i+1] = arr[i]
    		arr_data = ' '.join(map(str,arr))
    		print(arr_data)
    		if i == 0:
    			arr[i] = c_n
    			arr_data = ' '.join(map(str,arr))
    			print(arr_data)
    	else:
    		arr[i+1] = c_n
    		arr_data = ' '.join(map(str,arr))
    		print(arr_data)
    		break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
