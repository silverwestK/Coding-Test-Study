def decentNumber(n):
    if n % 3 == 0:
        return int('5' * n)
    else:
        cnt_5, cnt_3 = n - 5, 5
        while cnt_5 > 0:
            if cnt_5 % 3 == 0 and cnt_3 % 5 == 0:
                return int('5' * cnt_5 + '3' * cnt_3)
            cnt_5, cnt_3 = cnt_5 - 5, cnt_3 + 5
        if n % 5 == 0:
            return int('3' * n)
    return -1

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(decentNumber(n))
