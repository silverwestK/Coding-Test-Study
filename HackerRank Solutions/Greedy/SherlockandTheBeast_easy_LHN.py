#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Write your code here
    q, r = divmod(n, 3)

    if q != 0 or r % 5 == 0:
        for i, j in enumerate(range(q, -1, -1)):
            new_r = (i * 3) + r
            if new_r % 5 == 0:
                print('5' * (j * 3) + '3' * new_r)
                break
        else:
            print(-1)

    else:
        print(-1)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
