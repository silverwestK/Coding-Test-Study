#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
#
def candies(n, arr):
    # Write your code here
    # candy sorting
    sorted_candy = []
    answer = [0] * n
    for i, j in enumerate(arr):
        sorted_candy.append((i, j))
    sorted_candy.sort(key=lambda x: x[1])
    sorted_candy = dict(sorted_candy)

    # make answer list
    for key in sorted_candy:
        before = answer[key - 1] if key and sorted_candy[key] > sorted_candy[key - 1] else 0
        after = answer[key + 1] if key < n - 1 and sorted_candy[key] > sorted_candy[key + 1] else 0
        answer[key] = max(before, after) + 1

    return sum(answer)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
