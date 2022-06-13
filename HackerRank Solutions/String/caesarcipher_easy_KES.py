import os

def caesarCipher(s, k):
    res = ''
    for c in s:
        if c.islower():
            m, d = divmod(ord(c)+k%26, 123)
            res += chr([0,1][bool(m)] * 97 + d)
        elif c.isupper():
            m, d = divmod(ord(c)+k%26, 91)
            res += chr([0,1][bool(m)] * 65 + d)
        else:
            res += c
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

