#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting(unsorted):
    # Write your code here
    unsorted.sort(key=int)
    for i in unsorted:
        print(i)


if __name__ == '__main__':

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)
    print(result)

