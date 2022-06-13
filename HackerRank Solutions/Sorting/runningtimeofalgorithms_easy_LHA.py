#!/bin/python3
import os

def runningTime(arr):
    cnt = 0
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
            cnt += 1
        arr[j + 1] = key

    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
