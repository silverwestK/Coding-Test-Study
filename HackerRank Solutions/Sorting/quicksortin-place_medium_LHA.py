def quicksort(arr, start, end):
    if end - start > 1:
        a = arr[end-1]
        s = start
        for i in range(start, end):
            if a >= arr[i]:
                arr[s], arr[i] = arr[i], arr[s]
                s += 1
        print(*arr)
        arr = quicksort(arr, start, s-1)
        arr = quicksort(arr, s, end)
    return arr

n = int(input())
arr = list(map(int, input().split(' ')))
quicksort(arr, 0, n)