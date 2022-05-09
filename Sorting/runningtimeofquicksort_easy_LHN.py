import math
import os
import random
import re
import sys

global count
count = 0

def insertion_sort(l):
    count = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           count = count + 1
        l[j+1] = key
    return count


def partition(arr, start, end):
    global count
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            #swap
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            count = count + 1
    #pivot swap
    temp = arr[i + 1]
    arr[i + 1] = arr[end]
    arr[end] = temp
    count = count + 1
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

    b = arr[:]

    insert_count = insertion_sort(arr)
    arr = quicksort(b,0,n-1)
    print(insert_count - count)