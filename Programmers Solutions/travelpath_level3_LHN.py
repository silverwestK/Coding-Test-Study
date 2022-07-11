def dfs(tickets, route):
    print('tickets',tickets)
    print('route',route)
    if len(tickets) == 0:
        return route
    k = 0
    for i in tickets:
        if i[0] == route[-1]:
            break
        k = k + 1
    if k == len(tickets):
        return []
    while tickets[k][0] == route[-1]:
        result = dfs(tickets[:k] + tickets[k + 1:], route + [tickets[k][1]])
        if result != []:
            return result
        k = k + 1
    return result

def solution(tickets):
    tickets.sort(key= lambda x :(x[0],x[1]))
    route = ["ICN"]
    result = dfs(tickets, route)
    return result