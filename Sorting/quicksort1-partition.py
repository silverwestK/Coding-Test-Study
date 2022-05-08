#!/bin/python3
import os

def quickSort(arr):
    pivot = arr[0]
    left, right = [], []
    equal = [arr[0]]
    for i in arr[1:] :
        if i < pivot :
            left.append(i)
        elif i > pivot :
            right.append(i)
        elif i == pivot :
            equal.append(i)

    return left + equal + right

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
