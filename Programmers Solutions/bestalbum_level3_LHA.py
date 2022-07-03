from collections import defaultdict

def solution(genres, plays):
    answer = []

    sort_list = list(zip(list(range(len(genres))), genres, plays))
    sort_list.sort(key=lambda x: x[2], reverse=True)

    gen_dic = defaultdict(dict)
    set_gen = set(genres)
    for gen in set_gen:
        gen_dic[gen]['total_p'] = 0
        gen_dic[gen]['songs'] = []

    for i, g, p in sort_list:
        gen_dic[g]['total_p'] += p
        gen_dic[g]['songs'].append(i)

    gen_dic = sorted(gen_dic.items(), key=lambda x: x[1]['total_p'], reverse=True)
    for gen, dic in gen_dic:
        if len(dic['songs']) <= 2:
            answer.extend(dic['songs'])
        else:
            answer.extend(dic['songs'][:2])

    return answer
