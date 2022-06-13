#!/bin/python3
import os

def balancedSums(arr):
    arr_sum = sum(arr)
    left_sum = 0

    for i in range(n):
        arr_sum -= arr[i]
        if arr_sum == left_sum:
            return 'YES'
        left_sum += arr[i]

    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
