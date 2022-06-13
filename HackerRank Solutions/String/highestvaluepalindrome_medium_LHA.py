#!/bin/python3
import os

def highestValuePalindrome(s, n, k):
    mid = n // 2

    if n <= k:
        return '9' * n
    left = list(s[:mid])
    center = ''
    if n % 2 == 0:
        right = list(s[mid:])
    else:
        right = list(s[mid + 1:])
        center = s[mid]
    right = right[::-1]

    diff = [0 if l == r else 1 for l, r in zip(left, right)]
    diff_num = sum(diff)

    if diff_num > k:
        return '-1'

    count = k - diff_num
    for i in range(mid):
        if left[i] != right[i] and count != 0:
            if left[i] != '9' and right[i] != '9':
                count -= 1
            left[i] = '9'
            right[i] = '9'
        elif left[i] != right[i] and count == 0:
            left[i] = max(left[i], right[i])
            right[i] = max(left[i], right[i])
        elif left[i] == right[i] and count > 1 and left[i] != '9':
            left[i] = '9'
            right[i] = '9'
            count -= 2
        else:
            continue

    if count > 0 and n % 2 == 1:
        center = '9'

    return ''.join(left + list(center) + right[::-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
