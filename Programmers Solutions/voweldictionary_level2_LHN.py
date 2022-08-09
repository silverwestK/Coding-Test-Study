"""
A, AA, AAA, AAAA, AAAAA,
AAAAE, AAAAI, AAAAO, AAAAU,
AAAE, AAAEE, AAAEI, AAAEO, AAAEU,
AAAI, AAAIE, AAAII, AAAIO, AAAIU,
전체 경우의 수 : 5 + 25 + 125 + 625 + 3125
첫번째 자리 간격 : 781(3905/5)
두번째 자리 간격 : 156(3905/25)
세번째 자리 간격 : 31(3095/125)
네번째 자리 간격 : 6(3905/625)
다섯번째 자리 간격 : 1(3905/3125)
"""

def solution(word):
    answer = 0
    all_case = 5**1 + 5**2 + 5**3 + 5**4 + 5**5
    interval = [all_case//(5**1), all_case//(5**2), all_case//(5**3), all_case//(5**4), all_case//(5**5)]
    alpha = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    word = list(word)
    location = 0
    for i in range(len(word)):
        location = location + interval[i]*alpha[word[i]] + 1
    return location