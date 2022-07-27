# 문제: 전력망을 둘로 나누기
from collections import defaultdict
def bfs(tree):
    parent_nodes, visited_nodes = {1}, []
    while parent_nodes:
        tp = parent_nodes.pop()
        visited_nodes.insert(0, tp)
        parent_nodes.update(tree[tp])
        for c in tree[tp]:
            tree[c].remove(tp)
    return visited_nodes

def solution(n, wires):
    tree = defaultdict(list)
    for u, v in wires:
        tree[u].append(v)
        tree[v].append(u)

    visited_nodes = bfs(tree)
    cumulative_sums = [1] * n
    for node in visited_nodes:
        cumulative_sums[node - 1] += sum(cumulative_sums[c - 1] for c in tree[node])
    return min(abs(cumulative_sums[0] - 2 * cumulative_sums[i]) for i in range(1, n))