def solution(numbers):
    strNumbers = [str(n) for n in numbers]
    strNumbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(strNumbers)))