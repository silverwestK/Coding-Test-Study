

def solution(clothes):
    from itertools import combinations
    category = {}
    for i in clothes:
        if i[1] in category.keys():
            category[i[1]] = category[i[1]] + 1
        else:
            category[i[1]] = 1
    if len(category.keys()) > 1:
        answers = 1
        for i in category.values():
            answers = answers * (i+1)
        return answers -1
    else:
        return len(clothes)