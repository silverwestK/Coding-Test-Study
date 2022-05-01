#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    # Write your code here
    a_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    n = len(s)
    if n % 2 == 0:
    	f_s = s[0:n//2]
    	b_s = s[n//2:]
    else:
    	f_s = s[0:n//2]
    	b_s = s[n//2+1:]
    result = 0
    for i in range(len(f_s)):
    	result = result + abs(a_list.index(f_s[i]) - a_list.index(b_s[len(b_s) -1 - i]))
    return result

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(str(result)+'\n')
