# Lomuto Partitioning
def quickSort(arr, l , r):
    if l >= r or l < 0:
        return

    arr, p = partition(arr, l, r)
    quickSort(arr, l, p-1)
    quickSort(arr, p+1, r)

def partition(arr, l, r):
    i, pivot = l-1, arr[r]
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[r] = arr[r], arr[i]
    print(*arr)
    return arr, i

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().split()))
    
    quickSort(arr, 0, len(arr)-1)
