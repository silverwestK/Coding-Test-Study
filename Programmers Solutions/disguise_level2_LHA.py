from functools import reduce

def solution(clothes):
    cate = {}

    for _, c in clothes:
        if c not in cate:
            cate[c] = 2
        else:
            cate[c] += 1

    answer = reduce(lambda acc, cur: acc * cur, cate.values(), 1)

    return answer - 1