#!/bin/python3

import os

def funnyString(s):
    reverse_s = s[::-1]

    ori_ord = list(map(lambda x: ord(x), s))
    rev_ord = list(map(lambda x: ord(x), reverse_s))

    ori_ord = [abs(ori_ord[i + 1] - ori_ord[i]) for i in range(len(ori_ord) - 1)]
    rev_ord = [abs(rev_ord[i + 1] - rev_ord[i]) for i in range(len(rev_ord) - 1)]

    if ori_ord == rev_ord:
        return 'Funny'
    else:
        return 'Not Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
