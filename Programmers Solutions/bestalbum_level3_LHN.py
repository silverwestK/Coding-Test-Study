"""
문제 : 각 장르 별로 가장 많이 재생된 2개의 곡의 번호를 출력하는 것
조건 : 더 많이 재생된 장르 먼저 순서대로 나열한다
아이디어 :
이중 딕셔너리 사용
"""
def solution(genres, plays):
    #이중 dict 생성
    gens = list(set(genres))
    what = [{} for i in range(len(gens))]
    music_dict = dict(zip(gens, what))
    indexs = [i for i in range(len(plays))]
    for gen, play, index in zip(genres, plays, indexs):
        music_dict[gen][index] = play
    music_dict = list(music_dict.values())

    #장르별 합으로 정렬
    music_dict.sort(key = lambda x : sum(x.values()), reverse = True)

    #장르별로 큰것부터 정렬
    music_list = []
    for i in music_dict:
        print(list(i.items())[0])
        result = sorted(list(i.items()),key=lambda x: x[1], reverse = True)
        music_list.append(result)

    #answer 에 큰것 부터 2개씩 넣기
    answer = []
    for i in music_list:
        if len(i) < 2:
            for j in i:
                answer.append(j[0])
        else:
            for j in range(0,2):
                answer.append(i[j][0])

    return answer