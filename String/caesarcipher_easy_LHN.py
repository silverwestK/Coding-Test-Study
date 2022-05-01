#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    a_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
    result = ''
    l_s = s.lower()
    for i in range(len(l_s)):
        if l_s[i] in a_list:
            num = a_list.index(l_s[i]) + k
            if num > 25:
                num = num % 26
            if s[i].isupper():
                result = result + a_list[num].upper()
            else:
                result = result + a_list[num]
        else:
            result = result + l_s[i]
    return result


if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)
