"""
문제 :
문자열이 들어오면 그 문자열의 조합중에서 소수인것들의 수를 세는 문제
아이디어 :
1. prime 인지 검사하는 함수 생성
2. 문자열로 생성할 수 있는 모든 조합 생성
3. for 문을 돌리면서 확인
"""
def isprime(number):
    if number[0] == '0':
        return False
    number = int(number)
    if number == 1:
        return False
    else:
        for i in range(2,round(number**0.5)+1):
            if number % i == 0:
                return False
        return True

def solution(numbers):
    #순서가 있는 조합이기 때문에 순열 사용
    from itertools import permutations
    answer = 0
    for i in range(1,len(numbers)+1):
        number_list = set(permutations(numbers,i))
        for j in number_list:
            check_number = ''.join(j)
            if isprime(check_number):
                answer = answer + 1
    return answer