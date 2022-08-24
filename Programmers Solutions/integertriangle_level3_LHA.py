def solution(triangle):

    h = len(triangle) - 1
    while h > 0:
        for i in range(h):
            triangle[h-1][i] += max([triangle[h][i], triangle[h][i+1]])
        h -= 1

    answer = triangle[0][0]
    return answer
