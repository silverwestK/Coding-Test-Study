"""
문제 :
입력으로 문자열을 요소로 가지고 있는 리스트가 들어오면 각 요소를 부분문자열로
포함하고 있는 문자열이 있는지 여부를 확인한다.

아이디어:
문자열의 길이로 소팅을 시킨다.
for 문을 통해 확인한다.
"""
def solution(phone_book):
    answer = True
    phone_book.sort()
    n = len(phone_book)
    for i, j in zip(phone_book, phone_book[1:]):
        if len(i) < len(j):
            if j.startswith(i):
                answer = False
                return answer
    return answer