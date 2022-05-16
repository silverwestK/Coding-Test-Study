import math
import os
import random
import re
import sys



def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            #swap
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    #pivot swap
    temp = arr[i + 1]
    arr[i + 1] = arr[end]
    arr[end] = temp
    print(' '.join(map(str,arr)))
    return i + 1

def quicksort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        #left
        quicksort(arr, start, p - 1)
        #right
        quicksort(arr, p + 1, end)

    return arr



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quicksort(arr,0,n-1)


