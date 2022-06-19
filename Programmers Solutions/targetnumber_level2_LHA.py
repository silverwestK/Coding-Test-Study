answer = 0
def dfs(numbers, target, idx, val_sum):
    global answer
    leng = len(numbers)

    if val_sum == target and idx == leng:
        answer += 1
        return
    if idx == leng:
        return

    dfs(numbers, target, idx + 1, val_sum + numbers[idx])
    dfs(numbers, target, idx + 1, val_sum - numbers[idx])


def solution(numbers, target):
    global answer

    dfs(numbers, target, 0, 0)

    return answer