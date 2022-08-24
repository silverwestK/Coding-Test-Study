# 문제: 정수 삼각형
def solution(triangle):
    depth = len(triangle)
    for floorNum in range(depth-1, 0, -1):
        for i in range(floorNum):
            triangle[floorNum-1][i] += max(triangle[floorNum][i], triangle[floorNum][i+1])
    return triangle[0][0]