"""
아이디어 :
1. 리스트 요소의 가장 앞자리 크기로 소팅
2.
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))