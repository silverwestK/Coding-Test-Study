#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    # Write your code here
    """
    case1 :time out
    r_s1 = set(list(s1))
    r_s2 = set(list(s2))
    c_s1 = []
    c_s2 = []

    for i in s1:
    	if i in r_s2:
    		c_s1.append(i)
    for j in s2:
    	if j in r_s1:
    		c_s2.append(j)

    s1_list = [[]]
    s1_list_j = []
    for i in range(len(c_s1)):
    	s1_len = len(s1_list)
    	for j in range(s1_len):
    		factor = s1_list[j] + [c_s1[i]]
    		s1_list.append(factor)
    		s1_list_j.append(''.join(factor))

    s2_list = [[]]
    s2_list_j = []
    for i in range(len(c_s2)):
    	s2_len = len(s2_list)
    	for j in range(s2_len):
    		factor = s2_list[j] + [c_s2[i]]
    		s2_list.append(factor)
    		s2_list_j.append(''.join(factor))


    s1_set = set(s1_list_j)
    s2_set = set(s2_list_j)

    candi_list = s1_set & s2_set

    if len(candi_list) != 0:
    	max_len = len(max(candi_list,key=len))
    else:
    	max_len = 0

    return max_len
    """

    l_s1 = len(s1)
    l_s2 = len(s2)

    lcs_matrix = [[0]*(l_s2+1) for i in range(l_s1 + 1)]

    for i in range(1, l_s1 + 1):
        for j in range(1, l_s2 + 1):
            if s1[i-1] == s2[j-1]:
                lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1])

    return lcs_matrix[-1][-1]






if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    print(result)
