# 문제: 카펫
def solution(brown, yellow):
    grids = brown + yellow
    for i in range(round(grids**0.5), 2, -1):
        if grids%i == 0 and (grids//i-2)*(i-2) == yellow :
            return [grids//i, i]