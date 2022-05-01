#!/bin/python3

import os

def pangrams(s):
    ALPHA = [chr(i) for i in range(97,123)]
    s = list(set(s.replace(' ', '').lower()))
    s.sort()

    if ALPHA == s :
        return 'pangram'
    else :
        return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
