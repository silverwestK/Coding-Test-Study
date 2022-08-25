"""
"""


def solution(n, costs):
    from collections import deque
    vertices = {0}
    result = 0
    costs.sort(key=lambda e: e[2])
    while len(vertices) < n:
        for e in costs:
            if ((e[0] in vertices and e[1] not in vertices)
                    or (e[1] in vertices and e[0] not in vertices)):
                vertices.update(e[:2])
                result += e[2]
                break

    return result