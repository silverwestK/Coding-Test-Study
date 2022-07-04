"""
문제 : 현재 진행률과 하루동안의 작업 속도가 주어졌을 때 배포가 빠른 순서로 하루에 몇개씩 배포되는지 리스트로 반환
조건 : 무조건 앞에 있는 것 부터 반환 뒤쪽의 작업이 먼저 끝나도 앞에 있는 기능이 완료 되어야 같이 배포 가능
아이디어 :
각 작업이 얼마나 걸리는지 리스트를 만들어서 돌면서 배포가 얼마나 되는지 확인
"""
def solution(progresses, speeds):
    day_list = [(100 - i)//j if (100-i)%j == 0 else (100 - i)//j + 1 for i, j in zip (progresses,speeds)]
    answer = []
    count = 1
    for i in range(len(day_list)):
        if i+1 < len(day_list):
            if day_list[i] >= day_list[i+1]:
                day_list[i+1] = day_list[i]
                count = count + 1
            else:
                answer.append(count)
                count = 1
        else:
            answer.append(count)
    return answer