# Time Limit Exceeded except # 0,1,2,4
import os
import copy

def checkMoves(ipData):
    postsDic, mvCnt = ipData
    movesList = []
    for tpRods in range(1, 5):
        if postsDic[tpRods]:
            rods = [1,2,3,4]
            rods.remove(tpRods)
            for othRods in rods:
                if (not postsDic[othRods]
                        or postsDic[tpRods][0] < postsDic[othRods][0]):
                        movesList.append((postsDic, tpRods, othRods, mvCnt+1))
    return movesList

def moveDisk(postsDic, move):
    postsDic[move[1]].insert(0, postsDic[move[0]].pop(0))
    return postsDic

def bfs(n, postsDic):
    movesList = checkMoves((postsDic, 0))
    while movesList:
        postsDic, tpRods, othRods, mvCnt = movesList.pop(0)
        tempDic = moveDisk(copy.deepcopy(postsDic), move=(tpRods, othRods))
        if len(tempDic[1]) == n:
            return mvCnt
        tempList = checkMoves((tempDic, mvCnt))
        movesList.extend(tempList)

def hanoi(n, posts):
    # postsDic => key: rod, values: disks
    postsDic = {1:[], 2:[], 3:[], 4:[]}
    for i, p in enumerate(posts):
        postsDic[p].append(i+1)
    return bfs(n, postsDic)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    loc = list(map(int, input().rstrip().split()))

    res = hanoi(n, loc)

    fptr.write(str(res) + '\n')

    fptr.close()
