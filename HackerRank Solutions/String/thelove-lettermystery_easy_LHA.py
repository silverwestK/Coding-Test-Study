#!/bin/python3

import os

def theLoveLetterMystery(s):
    if len(s) == 1:
        return 0
    else:
        mid = len(s) // 2
        left = s[:mid]
        if len(s) % 2 == 1:
            right = s[mid + 1:]
        elif len(s) % 2 == 0:
            right = s[mid:]

        right = right[::-1]

        if left == right:
            return 0
        else:
            diff = list(map(lambda l, r: ord(l) - ord(r) if l > r else ord(r) - ord(l), left, right))
            return sum(diff)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
