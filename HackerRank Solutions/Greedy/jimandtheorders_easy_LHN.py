#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    # Write your code here
    for i, v in enumerate(orders):
        orders[i] = [i + 1, v[0] + v[1]]
    orders.sort(key=lambda x: x[1])
    for i in range(len(orders)):
        orders[i] = orders[i][0]
    return orders


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
