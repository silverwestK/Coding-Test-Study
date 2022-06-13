#!/bin/python3

def insertionSort2(n, arr):
    for i in range(1, n) :
        if max(arr[:i]) < arr[i]  :
            print(*arr)
        elif max(arr[:i]) >= arr[i] :
            temp = arr[:i]
            for j in range(len(temp)-1,-1,-1) :
                if arr[i] < arr[j] :
                    k = arr[i]
                    arr[i] = arr[j]
                    arr[j] = k
                    i = i - 1
                elif arr[i] >= arr[j] :
                    pass
            print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
