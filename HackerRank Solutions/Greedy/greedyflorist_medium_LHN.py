#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def buy_flower(total, r_time, left_flower, k):
    if k >= len(left_flower):
        for i in left_flower:
            total = total + (r_time + 1) * i
        return total
    else:
        for i in left_flower[0:k]:
            total = total + (r_time + 1) * i
        return buy_flower(total, r_time + 1, left_flower[k:], k)


def getMinimumCost(k, c):
    n = len(c)
    if k >= n:
        return sum(c)
    else:
        c.sort(reverse=True)
        total = sum(c[0:k])
        left_flower = c[k:]
        result = buy_flower(total, 1, left_flower, k)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
