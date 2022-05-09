#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

def initialize(s):
    n, z = len(s), ord('a')
    S, F, I = [[0] * L for _ in range(n + 1)], [1] * n, [1] * n
    # 문자열 각 자리별로 알파벳 몇개씩 들어있는지 알기 위한 이중 리스트 생성
    for i in range(1, n + 1):
        S[i][ord(str(s[i - 1])) - ord('a')] += 1
        if i + 1 < n + 1:
            S[i + 1] = S[i][:]
    for i in range(1, n):
        # 문자열 길이만큼의 팩토리얼을 미리 구해 둠
        F[i] = F[i - 1] * i % M
        # 팩토리얼 값의 모듈로 역수를 미리 구해 둠
        I[i] = pow(F[i], M - 2, M)
    return (S, F, I)


def answerQuery(l, r):
    c, s, d = 0, 0, 1
    # 부분 문자열 안에 알파벳 몇개씩 있는지 카운트 한 리스트
    s_list = []
    for i in range(L):
        s_list.append(S[r][i] - S[l - 1][i])
    for j in s_list:
        # 가운데에 위치 할 홀수개를 가진 알파벳 개수
        c += j % 2
        # 조합 해볼 수 있는 알파벳의 수(예: aaabbbb -> abb)
        s += j // 2
        # 모듈로 나눗셈 계산을 위한 모듈로 역원 계산
        d *= I[j // 2]
    # 가운데에 위치할 수 있는 알파벳 수 * 조합할 수 있는 알파벳 팩토리얼 * 모듈로 역원들 곱셈 값 % M
    return ((c or 1) * F[s] * d % M)


import os

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    L, M = 26, 1000000007
    S, F, I = initialize(input())
    for _ in range(int(input())):
        result = answerQuery(*map(int, input().split()))
        fptr.write(str(result) + '\n')
    fptr.close()

