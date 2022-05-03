import os

def highestValuePalindrome(s, n, k):
    s_lis = list(map(int, s))
    changed = [0] * (round(n/2) + 1)

    i = 0
    while k > 0 and i < round(n/2):
        if s_lis[i] != s_lis[-i - 1]:
            max_val = max(s_lis[i], s_lis[-i - 1])
            s_lis[i] = s_lis[-i - 1] = max_val
            changed[i] = 1
            k -= 1
        i += 1

    i = 0
    while k > 0 and i < round(n/2)+1:
        if s_lis[i] != 9:
            if True not in changed and k == 1:
                s_lis[round(n/2)] = 9
            else:
                s_lis[i] = s_lis[-i - 1] = 9
                k -= (2 - changed[i])
        i += 1

    res = ''.join(map(str, s_lis))
    return '-1' if res != res[::-1] else res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
