import os


def insertion_sort(arr):
    cnt = 0
    for end in range(1, len(arr)):
        target = arr[end]
        i = end
        while i > 0 and arr[i - 1] > target:
            arr[i] = arr[i - 1]
            i, cnt = i - 1, cnt + 1
        arr[i] = target
    return cnt


def quick_sort(arr):
    global cnt
    cnt = 0

    def sort(low, high):
        if low >= high:
            return
        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid + 1, high)

    def partition(low, high):
        global cnt
        pivot = arr[high]
        pt = low
        for i in range(low, high):
            if arr[i] <= pivot:
                arr[pt], arr[i] = arr[i], arr[pt]
                pt, cnt = pt + 1, cnt + 1
        arr[pt], arr[high] = arr[high], arr[pt]
        cnt += 1
        return pt

    sort(0, len(arr) - 1)
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = insertion_sort(arr.copy()) - quick_sort(arr.copy())

    fptr.write(str(result) + '\n')

    fptr.close()
