#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here
    s=list(s)
    if n<=k:
        return '9'*n
    mink=[0]*(n//2+1)
    for i in range(n//2-1,-1,-1):
        if s[i]!=s[n-1-i]:
            mink[i]=mink[i+1]+1
        else:
            mink[i]=mink[i+1]
    if mink[0]>k:
        return '-1'
    i=0
    while i<n//2 and k>=mink[i]:
        if s[i]=='9':
            if s[n-1-i]!='9':
                s[n-1-i]='9'
                k-=1
        elif s[n-1-i]=='9':
            s[i]='9'
            k-=1
        elif k-2>=mink[i+1]:
            s[i]=s[n-1-i]='9'
            k-=2
        else:
            if s[i]!=s[n-1-i]:
                s[i]=s[n-1-i]=max(s[n-1-i],s[i])
                k-=1
        i+=1
    if n%2:
        if k>0:
            s[n//2]='9'
    return ''.join(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
