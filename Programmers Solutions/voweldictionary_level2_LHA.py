from itertools import product

def solution(word):
    chars = ['A', 'E', 'I', 'O', 'U']

    permu = []
    for i in range(1, 6):
        permu += list(product(chars, repeat=i))
    permu = [''.join(c) for c in permu]
    permu.sort()
    return permu.index(word) + 1