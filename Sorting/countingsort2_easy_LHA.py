#!/bin/python3
import os

def countingSort(arr):
    frequency = [0] * 100
    for i in arr:
        frequency[i] += 1

    sorted_arr = []
    for idx, d in enumerate(frequency):
        sorted_arr.extend([idx] * d)

    return sorted_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
