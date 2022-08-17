# 문제: 구명보트
def solution(people, limit):
    answer = 0
    people.sort()
    i, j = 0, len(people) - 1

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        answer += 1
    return answer