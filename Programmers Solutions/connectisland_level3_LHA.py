def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    total_w = 0
    parent = [0] * (n + 1)

    for i in range(n + 1):
        parent[i] = i

    costs.sort(key=lambda x: x[2])

    for cost in costs:
        n1, n2, w = cost
        if find_parent(parent, n1) != find_parent(parent, n2):
            union_parent(parent, n1, n2)
            total_w += w

    return total_w