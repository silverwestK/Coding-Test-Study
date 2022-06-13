#!/bin/python3

import os
import collections

def steadyGene(gene):
    leng = len(gene) // 4
    cnt = {'C': 0, 'A': 0, 'T': 0, 'G': 0}
    cnt.update(collections.Counter(gene))

    if all(map(lambda x: x == leng, cnt.values())):
        return 0

    low, high = 0, len(gene)
    while high - low > 1:
        mid = (high + low) // 2
        cnt_tmp = dict(cnt)
        for i in range(mid):
            cnt_tmp[gene[i]] -= 1
        if all(map(lambda x: x <= leng, cnt_tmp.values())):
            high = mid
            continue
        for i in range(mid, len(gene)):
            cnt_tmp[gene[i - mid]] += 1
            cnt_tmp[gene[i]] -= 1
            if all(map(lambda x: x <= leng, cnt_tmp.values())):
                high = mid
                break
        else:
            low = mid
    return high


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
