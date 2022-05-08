#!/bin/python3
import os

def marsExploration(s):
    num = len(s) // 3
    cnt = 0
    for i in range(0, num):
        for c1, c2 in zip(s[3 * i:3 * i + 3], 'SOS'):
            if c1 != c2:
                cnt += 1
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
