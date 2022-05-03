def insertionSort2(n, arr):
    for end in range(1,n):
        target = arr[end]
        i = end
        while i > 0 and arr[i-1] > target:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
        arr[i] = target
        for val in arr:
            print(val, end=' ')
        print()

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)