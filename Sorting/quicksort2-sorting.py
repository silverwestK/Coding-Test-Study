def quicksort(ar):
    if len(ar) < 2:
        return ar
    pivot = ar[0]
    left, right = [], []
    equal = [ar[0]]
    for i in ar[1:]:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        elif i == pivot:
            equal.append(i)

    rec = quicksort(left) + equal + quicksort(right)
    print(*rec)
    return rec


n = int(input().strip())
ar = list(map(int, input().rstrip().split()))
quicksort(ar)
