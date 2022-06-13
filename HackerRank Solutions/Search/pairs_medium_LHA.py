#!/bin/python3
import os
from collections import Counter


def pairs(k, arr):
    cnt = Counter(arr)
    answer = 0
    for i in arr:
        if (i - k) in cnt:
            answer += 1

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
