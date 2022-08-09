# 문제: 큰 수 만들기
def solution(number, k):
    answer = []
    for n in number:
        while answer and k > 0 and n > answer[-1]:
            answer.pop()
            k -= 1
        answer.append(n)
    return ''.join(answer[:len(number) - k])