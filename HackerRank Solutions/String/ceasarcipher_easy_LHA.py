#!/bin/python3

import os

def caesarCipher(s, k):

    result = list(map(lambda x: chr((ord(x) - ord('a') + k) % 26 + ord('a')) if x.islower() else x, s))
    result = list(map(lambda x: chr((ord(x) - ord('A') + k) % 26 + ord('A')) if x.isupper() else x, result))

    return ''.join(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
