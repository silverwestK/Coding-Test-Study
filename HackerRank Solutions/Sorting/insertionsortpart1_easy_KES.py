def insertionSort1(n, arr):
    for end in range(1, n):
        target = arr[end]
        i = end
        while i > 0 and arr[i - 1] > target:
            arr[i] = arr[i - 1]
            i -= 1
            print(*arr)
        arr[i] = target
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
