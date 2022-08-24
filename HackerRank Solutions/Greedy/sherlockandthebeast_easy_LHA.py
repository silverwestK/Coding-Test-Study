#!/bin/python3

def decentNumber(n):
    q3 = n // 3
    q5 = n // 5

    for i in range(0, q5 + 1):
        for j in range(q3 + 1, -1, -1):
            if 5 * i + 3 * j == n:
                return print('555' * j + '33333' * i)

    print(-1)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
