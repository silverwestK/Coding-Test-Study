# Solution 1: Hash
def solution(phone_book):
    pbDic = {}
    for pn in phone_book:
        pbDic[pn] = 1
    for pn in phone_book:
        for i in range(1, len(pn)):
            if pn[:i] in pbDic:
                return False
    return True

# Solution 2: String
def solution(phone_book):
    phone_book.sort()
    for a, b in zip(phone_book[:-1], phone_book[1:]):
        if b.startswith(a):
            return False
    return True