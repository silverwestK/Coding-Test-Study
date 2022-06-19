def solution(phone_book):
    answer = True
    hashMap = {}

    for number in phone_book:
        hashMap[number] = 1

    for number in phone_book:
        prefix = ''
        for n in number:
            prefix += n
            if prefix in hashMap and prefix != number:
                return False

    return answer