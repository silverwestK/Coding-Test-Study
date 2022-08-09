def solution(number, k):
    answer = []
    lens = len(number) - k
    for i in number:
        if len(answer) == 0:
            answer.append(i)
            continue
        while answer[-1] < i and k > 0:
            answer.pop()
            k = k - 1
            if len(answer) == 0 or k <= 0 or i == 9:
                break
        answer.append(i)
        if len(answer) == len(number) - k:
            break
    if k > 0:
        answer = answer[0:lens]
    return ''.join(answer)