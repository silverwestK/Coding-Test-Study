#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    s_list = []
    for i in s:
    	s_list.append(ord(i))
    s_c_list = []
    for i in range(len(s_list)-1):
    	s_c_list.append(abs(s_list[i] - s_list[i+1]))
    if s_c_list == list(reversed(s_c_list)):
    	return 'Funny'
    else:
    	return 'Not Funny'

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        print(result)


