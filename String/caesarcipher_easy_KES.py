#!/bin/python3

import os

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

# ASCII Code
# 'a': 97, 'z':122
# 'A': 65, 'Z':90

def caesarCipher(s, k):
    res = ''
    for c in s:
        if c.islower():
            m, d = divmod(ord(c)+k%26, 123)
            res += chr([0,1][bool(m)] * 97 + d)
        elif c.isupper():
            m, d = divmod(ord(c)+k%26, 91)
            res += chr([0,1][bool(m)] * 65 + d)
        else:
            res += c
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

