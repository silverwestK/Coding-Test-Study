def solution(brown, yellow):
    total = brown + yellow
    for w in range(round(total**0.5),2,-1) :
        if total % w == 0 :
            h = total // w
            if yellow == (w-2)*(h-2) :
                return [w,h]
