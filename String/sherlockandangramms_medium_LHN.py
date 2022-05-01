#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    result = 0
    while len(s) >= 1:
    	f_n = s[0]
    	s_l = s[1:]
    	for i in range(len(s_l)):
    		s_list = []
    		for k in range(len(s_l)):
    			merging = "".join(sorted(s_l[k:k+i+1]))
    			s_list.append(merging)
    		result = result + s_list.count(f_n)
    		if len(f_n) < len(s):
    			f_n = f_n + s[i+1]
    			f_n = "".join(sorted(f_n))
    	s = s[1:]
    return result

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)


