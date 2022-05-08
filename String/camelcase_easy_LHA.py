#!/bin/python3
import os

def camelcase(s):
    cnt = 0
    for c in s:
        if c.isupper():
            cnt += 1
    return cnt + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
