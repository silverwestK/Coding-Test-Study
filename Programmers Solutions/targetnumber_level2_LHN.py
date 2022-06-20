"""
문제:
사용할 수 있는 숫자들이 주어지고 각 숫자들을 한번씩 사용하여 사칙 연산으로
타겟 넘버를 만들 수 있는 횟수를 리턴하는 문제이다.

아이디어:
각 숫자는 +숫자 또는 -숫자 값을 가질 수 있다.
모든 경우를 체크하기 위해 bfs 가 적합하다고 생각한다.

경우가 나뉘기 때문에 q에 한 인덱스 마다 두개를 삽입한다 +일 경우 -일 경우
"""


def solution(numbers, target):
    from collections import deque
    answer = 0
    n = len(numbers)
    q = deque()
    q.append([numbers[0], 0])
    q.append([-1 * numbers[0], 0])
    while q:
        now_sum, index = q.popleft()
        index = index + 1
        if index < n:
            q.append([now_sum + numbers[index], index])
            q.append([now_sum - numbers[index], index])
        else:
            if now_sum == target:
                answer = answer + 1

    return answer