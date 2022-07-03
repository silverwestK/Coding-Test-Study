# 문제: 베스트앨범

def solution(genres, plays):
    streamingInfo = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        value = streamingInfo.get(g, [0, []])
        value[0] += p
        value[1].append((p, i))
        streamingInfo[g] = value

    answer = []
    for songs in sorted(streamingInfo.values(), reverse=True):
        songs[1].sort(key=lambda x:x[0], reverse=True)
        answer += [s[1] for s in songs[1][:2]]
    return answer