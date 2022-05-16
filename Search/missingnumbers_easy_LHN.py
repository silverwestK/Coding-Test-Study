#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    r_set = set(brr)
    f_set = set(arr)

    d_list = list(r_set - f_set)
    inter_list = list(r_set & f_set)

    for i in inter_list:
        r_c = brr.count(i)
        f_c = arr.count(i)
        if r_c != f_c:
            d_list.append(i)
    d_list.sort(key=int)
    return d_list


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(result)

