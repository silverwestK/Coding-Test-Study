#!/bin/python3
import os
import sys

# sol 1
def maxMin(k, arr) :
    ans = sys.maxsize
    arr.sort()
    for i in range(n-k+1) :
        # unfairness = arr[i:i+k][-1] - arr[i:i+k][0]
        unfairness = arr[i+k-1]-arr[i]
        if unfairness == 0 :
            return unfairness
        if unfairness < ans :
            ans = unfairness
    return ans

# sol 2
def maxMin(k, arr):
    arr.sort()
    return min([arr[x+k-1]-arr[x] for x in range(n-k+1)])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
