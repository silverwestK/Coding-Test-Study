def highestValuePalindrome(s, n, k):
    s_lis = list(map(int, s))
    changed = [0] * (round(n / 2) + 1)

    i = 0
    while k > 0 and i < round(n / 2):
        if s_lis[i] != s_lis[-i - 1]:
            max_val = max(s_lis[i], s_lis[-i - 1])
            s_lis[i] = s_lis[-i - 1] = max_val
            changed[i] = 1
            k -= 1
        i += 1

    i = 0
    while k > 0 and i < round(n / 2) + 1:
        if s_lis[i] != 9:
            if n % 2 != 0 and True not in changed and k == 1:
                s_lis[round(n / 2)] = 9
            elif n % 2 == 0 and True not in changed and k == 1:
                break
            else:
                s_lis[i] = s_lis[-i - 1] = 9
                k -= (2 - changed[i])
        i += 1

    res = ''.join(map(str, s_lis))
    print(res)
    return '-1' if res != res[::-1] else res