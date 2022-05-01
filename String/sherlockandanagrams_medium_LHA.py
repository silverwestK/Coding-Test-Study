#!/bin/python3

import math
import os
import random
import re
import sys
import collections
from itertools import combinations


#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# def sherlockAndAnagrams(s):
#     # Write your code here
#     TOTAL = 0
#     # anagrammatic pairs of length 1
#     counter = collections.Counter(s)
#     for char, cnt in counter.items():
#         if cnt > 1 :
#             idx_list = list(filter(lambda c: c == char, s))
#             combi_1 = list(combinations(idx_list, 2))
#             TOTAL += len(combi_1)
#     print('1:',TOTAL)
#     dic = {}
#     for i in range(2, len(s)) :
#         dic[i] = {}
#         all_combi = list(combinations(s,i))
#         for combi in all_combi :
#             sorted_combi_str = ''.join(sorted(combi))
#             combi_str = ''.join(combi)
#             if combi_str in s :
#                 # idx_list = list(filter(lambda c: c == char, s))
#                 if sorted_combi_str not in dic[i].keys():
#                     dic[i][sorted_combi_str] = [combi_str]
#                 else :
#                     dic[i][sorted_combi_str].append(combi_str)

#                 dic[i][sorted_combi_str] = list(set(dic[i][sorted_combi_str]))

#         for anag_list in dic[i].values() :
#             if len(anag_list) > 1  :
#                 print(anag_list)
#                 combi_n = list(combinations(anag_list, 2))
#                 TOTAL += len(combi_n)
#                 print(TOTAL)


#         # sorted_cnt = collections.Counter(all_combi)
#     print(dic)


#     return TOTAL

def sherlockAndAnagrams(s):
    # Write your code here
    TOTAL = 0
    ana_dict = {}
    for leng in range(1, len(s)):
        for i in range(len(s) - leng + 1):
            sub = ''.join(sorted(s[i:i + leng]))
            if sub in ana_dict.keys():
                TOTAL += ana_dict[sub]
                ana_dict[sub] += 1
            else:
                ana_dict[sub] = 1

    return TOTAL


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
