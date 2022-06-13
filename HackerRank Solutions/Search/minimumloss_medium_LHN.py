#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    new_price = []
    mins = sys.maxsize
    n = len(price)
    for i in range(n):
    	new_price.append([i,price[i]])
    new_price.sort(key = lambda x : x[1])

    for i in range(n-1):
    	if new_price[i][0] > new_price[i+1][0]:
    		mins = min(mins, (new_price[i+1][1] - new_price[i][1]))
    return mins


if __name__ == '__main__':

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    print(result)


