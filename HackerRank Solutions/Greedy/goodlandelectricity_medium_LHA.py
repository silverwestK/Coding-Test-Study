#!/bin/python3
import os

def pylons(k, arr):
    leng = len(arr)
    start = 0
    last_pylon = -1

    total_pylons = 0
    while (start < leng):
        furthest = min(start + k - 1, leng - 1)

        for i in range(furthest, last_pylon, -1):
            if arr[i]:
                total_pylons += 1
                start = i + k
                last_pylon = i
                break
        else:
            return -1

    return total_pylons

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
