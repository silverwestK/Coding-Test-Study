#!/bin/python3
import os

def luckBalance(k, contests):
    contests.sort(key=lambda x: x[0], reverse=True)
    ans = 0
    for l, t in contests:
        if t == 0:
            ans += l
        elif t == 1:
            if k != 0:
                ans += l
                k -= 1
            else:
                ans -= l
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
