def insertionSort1(n, arr):
    for end in range(1, n):
        target = arr[end]
        i = end
        while i > 0 and arr[i - 1] > target:
            arr[i] = arr[i - 1]
            i -= 1
            for val in arr:
                print(val, end= ' ')
            print()
        arr[i] = target
    for val in arr:
        print(val, end= ' ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
