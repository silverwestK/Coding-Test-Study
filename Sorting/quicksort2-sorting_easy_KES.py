def quick_sort(arr):
    pivot, *rest = arr
    left, right = [], []
    for i in rest:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    if len(left) > 1: left = quick_sort(left)
    if len(right) > 1: right = quick_sort(right)

    res = left + [pivot] + right
    print(*res)
    return res


def main():
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    quick_sort(arr)


main()