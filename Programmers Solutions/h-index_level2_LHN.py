"""
문제 :
숫자를 요소로 갖는 리스트가 인풋으로 주어질 경우 과반수 이상 넘은 값중 가장 큰 값을 리턴하는 것
아이디어 :
역순으로 소팅하여 크거나 같은 값이 절반 이상이면 그 값을 리턴
"""


def solution(citations):
    citations.sort(reverse=True)
    n = len(citations)
    check = n // 2 + n % 2
    answer = 0
    count_list = []
    for i in range(n):
        for j in range(n):
            if citations[j] >= citations[i]:
                answer = answer + 1
        if citations[i] >= answer:
            count_list.append(answer)
        else:
            count_list.append(0)
        answer = 0

    return max(count_list)