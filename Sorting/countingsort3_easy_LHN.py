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
    count = 0
    for i in range(0,len(c_list)):
        count = count + c_list[i]
        c_list[i] = count
    c_list = c_list + [c_list[-1]] * (100 - len(c_list))

    print(' '.join(map(str,c_list)))





if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for i in range(n):
        inputs = input()
        s_list = inputs.split()
        arr.append(int(s_list[0]))

    result = countingSort(arr)



