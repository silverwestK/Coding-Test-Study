#!/bin/python3

def insertionSort1(n, arr):
    k = arr[-1]
    for i in range(n-2, -1, -1) :
        if arr[i] > k :
            arr[i+1] = arr[i]
            print(*arr)
            arr[i] = k
            if i == 0 :
                print(*arr)
        elif arr[i] <= k :
            print(*arr)
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
