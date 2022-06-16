from itertools import permutations

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    generated = []
    for i in range(1, len(numbers)+1):
        for comb in permutations(numbers, i):
            generated.append(int(''.join(comb)))
    for gn in set(generated):
        if gn not in [0,1] and isPrime(gn):
            answer += 1
    return answer