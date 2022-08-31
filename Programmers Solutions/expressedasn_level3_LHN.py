"""
1개 사용할 경우 : n
2개 사용할 경우 : nn, n//n, nxn, n+n, n-n (1번 (사칙연산)  1번)
3개 사용할 경우 : (1번 (사칙연산) 1번 (사칙연산) 1번) , (2번 (사칙연산) 1번)
...
"""

def calculate_n(X, Y):
    n_set = set()
    for x in X:
        for y in Y:
            n_set.add(x+y)
            n_set.add(x-y)
            n_set.add(x*y)
            if y != 0:
                n_set.add(x//y)
    return n_set

def solution(N, number):
    answer = -1
    result = {}
    result[1] = {N}
    if number == N:
        return 1
    for n in range(2, 9):
        i = 1
        temp_set = {int(str(N)*n)}
        # 1 (op) N-1.... n-1 (op) 1 까지 계산
        while i < n:
            temp_set.update(calculate_n(result[i], result[n-i]))
            i += 1
        # 만들어진 셋에 원하는 숫자가 있으면 stop
        if number in temp_set:
            answer = n
            break

        result[n] = temp_set

    return answer
