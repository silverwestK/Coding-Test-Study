# try 1 : test case 1,2,11,12 만 통과
# from itertools import combinations
# def solution(number, k):
#     permu = list(combinations(number, len(number)-k))
#     return ''.join(max(permu))

# try 2
def solution(number, k):
    numbers = list(number)
    temp = [numbers.pop(0)]

    for n in numbers:
        if temp[-1] < n:
            while temp and temp[-1] < n and k > 0:
                temp.pop()
                k -= 1
            temp.append(n)
        elif temp[-1] >= n or k == 0:
            temp.append(n)

    if k != 0:
        temp = temp[:-k]

    return ''.join(temp)

