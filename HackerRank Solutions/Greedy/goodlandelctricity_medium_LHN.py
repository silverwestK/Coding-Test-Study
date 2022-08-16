#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    l_arr = len(arr)
    start = 0
    last_pylon = -1

    total_pylons = 0
    while (start < l_arr):
        furthest = min(start + k - 1, l_arr - 1)

        for i in range(furthest, last_pylon, -1):
            if arr[i]:
                total_pylons += 1
                start = i + k
                last_pylon = i
                break
        #for 문이 break 되지 않고 끝까지 진행되었을 경우
        else:
            return -1

    return total_pylons


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
