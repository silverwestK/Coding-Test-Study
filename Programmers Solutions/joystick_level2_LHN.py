"""
문제 : 조이스틱을 움직여서 이름을 만들 때 최소로 몇번 움직여야 하는지를 반환하는 문제
조이스틱 움직임
위 : 다음 알파벳
아래 : 이전 알파벳
왼 : 이전 글자로 이동
오 : 다음 글자로 이동
아이디어 :
현재 바꾼 위치에서 다음 바꿀 위치가 왼쪽으로 이동하는 것이 빠른지 오른쪽으로 이동하는 것이 빠른지 파악
글자를 변경하는 조이스틱 횟수와 다음으로 바꿀 글자를 정하는 조이스틱 횟수 분리시켜서 생각
JAANA
JANAAAN
(0)(2)(6)
[0,2,6]
왼쪽으로 가는 경우
1. cur < 해당 인덱스
cur -> 0까지 가는 거리 +  len(name) -> 해당 인덱스 까지 가는 거리
2. cur > 해당 인덱스
cur -> 해당 인덱스 까지 가는 거리
오른쪽으로 가는 경우
1. cur < 해당 인덱스
cur -> 해당 인덱스 까지 가는 거리
2. cur > 해당 인덱스
cur -> len(name) 까지 가는 거리 +  0 -> 해당 인덱스 까지 가는 거리
"""
def solution(name):
    from collections import deque
    import sys
    ap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    name = list(name)
    n = len(name)
    make = ['A']*n
    total = 0
    move = []
    for a,(i,j) in enumerate(zip(make, name)):
        if i == j:
            continue
        if a != 0:
            move.append(a)
        total = total + min((ap.index(j)), (26-ap.index(j)))
    q = deque()
    total2 = 0
    total2_list = []
    q.append([0,total2,move])
    while q:
        cur,totals,moves = q.popleft()
        if moves:
            for i in moves:
                if cur < i:
                    right = i - cur
                    left = cur - 0 + n - i
                else:
                    right = n - cur + i - 0
                    left = cur - i
                moving = min(right,left)
                totalq = totals + moving
                moving = moves[:]
                moving.remove(i)
                q.append([i,totalq,moving])
        else:
            total2_list.append(totals)
    return total + min(total2_list)