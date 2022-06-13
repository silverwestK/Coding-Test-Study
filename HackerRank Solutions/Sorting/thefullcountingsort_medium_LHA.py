#!/bin/python3

def countSort(arr):
    mid = n // 2
    for i in range(mid):
        arr[i][1] = '-'

    val_list = list(zip(*arr))[0]
    max_v = int(max(val_list))
    sorted_list = [[] for _ in range(max_v + 1)]

    for l in arr:
        sorted_list[int(l[0])].append(l[1])

    sorted_list = sum(sorted_list, [])
    print(*sorted_list)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
