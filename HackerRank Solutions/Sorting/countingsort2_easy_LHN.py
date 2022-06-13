#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    max_n = max(arr)
    c_list = [0]*(max_n+1)
    for i in arr:
    	c_list[i] = c_list[i] + 1
    r_list = []
    for i in range(0,len(c_list)):
        r_list = r_list + [i]*c_list[i]
    return r_list





if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(result)
