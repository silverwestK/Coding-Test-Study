#!/bin/python3
import os

def candies(n, arr):
    can1 = [1] * n
    can2 = [1] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            can1[i] = can1[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            can2[i] = can2[i + 1] + 1

    total = 0
    for i in range(n):
        total += max(can1[i], can2[i])
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
