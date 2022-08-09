# 문제: 모음 사전
from itertools import product

def solution(word):
    words = []
    for i in range(1, 6):
        prods = [''.join(p) for p in product(['A', 'E', 'I', 'O', 'U'], repeat=i)]
        words.extend(prods)
    words.sort()
    return words.index(word) + 1