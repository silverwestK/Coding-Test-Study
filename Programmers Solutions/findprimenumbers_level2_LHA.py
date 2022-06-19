from itertools import permutations

def solution(numbers):
    answer = 0
    nums = [n for n in numbers]

    all_permu = []
    for leng in range(1, len(nums) + 1):
        permu = list(permutations(nums, leng))
        for p in permu:
            temp = ''.join(list(p))
            all_permu.append(int(temp))

    all_permu = list(set(all_permu))
    for num in all_permu:
        if num == 0 or num == 1:
            continue
        count = 0
        for i in range(2, num):
            if num % i == 0:
                count = 1
                break
        if count == 0:
            answer += 1

    return answer