#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = s.lower()
    s = s.replace(' ','')
    s = set(list(s))
    a_set = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','x','y','z'])
    differ = len(a_set - s)
    if differ == 0:
    	return 'pangram'
    else:
    	return 'not pangram'

if __name__ == '__main__':

    s = input()

    result = pangrams(s)

    print(result)
