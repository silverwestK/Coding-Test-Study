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

    #case3
    if len(arr) < 2:
        return arr
    lt, eq, rt = [], [], []
    for item in arr:
        if item < arr[0]:
            lt.append(item)
        elif item > arr[0]:
            rt.append(item)
        else:
            eq.append(item)
    sub = quickSort(lt) + eq + quickSort(rt)
    print(' '.join([str(x) for x in sub]))
    return(sub)



if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    #result = quickSort(arr)



