def solution(people, limit):
    answer = 0
    people.sort()
    n = len(people)
    i, j = 0, n - 1
    while i <= j:
        if people[i] + people[j] > limit:
            answer += 1
            j = j - 1
        else:
            answer += 1
            i = i + 1
            j = j - 1

    return answer