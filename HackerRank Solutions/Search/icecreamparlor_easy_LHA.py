#!/bin/python3
import os
from itertools import combinations

def icecreamParlor(m, arr):
    arr = [(idx + 1, i) for idx, i in enumerate(arr)]
    combis = list(combinations(arr, 2))
    combis = [c for c in combis if c[0][1] + c[1][1] == m]

    return [combis[0][0][0], combis[0][1][0]]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
