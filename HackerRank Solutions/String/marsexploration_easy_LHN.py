#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    o_l = []
    s_l = []
    for i in range(len(s)):
    	if i % 3 == 1:
    		o_l.append(s[i])
    	else:
    		s_l.append(s[i])
    result = 0
    result = result + len(o_l) - o_l.count('O') + len(s_l) - s_l.count('S')
    return result


if __name__ == '__main__':

    s = input()

    result = marsExploration(s)

    print(result)
