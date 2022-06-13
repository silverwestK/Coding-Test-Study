#!/bin/python3
import os

def sherlockAndAnagrams(s):
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
