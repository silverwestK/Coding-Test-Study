def countSort(arr):
    maxVal = max([int(i) for i, _ in arr])

    result = [[] for _ in range(maxVal+1)]
    for idx, (i, s) in enumerate(arr):
        if idx < len(arr) // 2:
            result[int(i)].append('-')
        else:
            result[int(i)].append(s)
    print(' '.join([y for x in result for y in x]))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)