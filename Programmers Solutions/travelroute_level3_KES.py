from collections import defaultdict

def solution(tickets):
    airport = defaultdict(list)
    for f, t in tickets:
        airport[f].append(t)
    for ap in airport.keys():
        airport[ap].sort()

    stack, answer = ['ICN'], []
    while stack:
        tempAirport = stack[-1]
        if tempAirport not in airport or not bool(airport[tempAirport]):
            answer.append(stack.pop(-1))
        else:
            stack.append(airport[tempAirport].pop(0))

    return answer[::-1]