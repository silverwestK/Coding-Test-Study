def solution(N, number):
    sets = [0, [N]]
    if N == number:
        return 1

    for i in range(2, 9):
        case = []
        iter_num = int(str(N) * i)
        case.append(iter_num)
        for i_half in range(1, i // 2 + 1):
            for x in sets[i_half]:
                for y in sets[i - i_half]:
                    case.append(x + y)
                    case.append(x - y)
                    case.append(y - x)
                    case.append(x * y)
                    if y != 0:
                        case.append(x / y)
                    if x != 0:
                        case.append(y / x)

            if number in case:
                return i
            sets.append(case)

    return -1