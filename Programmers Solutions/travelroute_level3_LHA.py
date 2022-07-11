from collections import defaultdict

def solution(tickets):
    answer = []
    ticket_dic = defaultdict(list)

    for t in tickets:
        ticket_dic[t[0]].append(t[1])

    for r in ticket_dic:
        ticket_dic[r].sort(reverse=True)

    travel = ['ICN']
    while travel:
        start = travel[-1]
        if not ticket_dic[start]:
            answer.append(travel.pop())
        else:
            travel.append(ticket_dic[start].pop())

    answer.reverse()
    return answer