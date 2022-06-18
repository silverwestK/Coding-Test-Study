# Problem: Kruskal (MST): Really Special Subtree
import os

def graph_info(g_nodes, g_from, g_to, g_weight):
    parents = [i for i in range(g_nodes+1)]
    edges_info = [(g_weight[i], g_from[i], g_to[i]) for i in range(len(g_from))]
    edges_info.sort()
    return parents, edges_info

def find_parent(parents, n):
    if parents[n] != n:
        parents[n] = find_parent(parents, parents[n])
    return parents[n]

def union_parent(parents, up, vp):
    if up < vp:
        parents[vp] = up
    else:
        parents[up] = vp
    return parents

def kruskals(g_nodes, g_from, g_to, g_weight):
    parents, edges_info = graph_info(g_nodes, g_from, g_to, g_weight)
    total_weights = 0
    for w, u, v in edges_info:
        u_parent, v_parent = find_parent(parents, u), find_parent(parents, v)
        if u_parent != v_parent:
            parents = union_parent(parents, u_parent, v_parent)
            total_weights += w
    return total_weights

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)
    fptr.write(str(res))

    fptr.close()
