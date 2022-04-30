import os

def steadyGene(gene):
    gene_dic = {'A':0, 'C':0, 'G': 0, 'T':0}
    for c in gene: gene_dic[c]+=1
    gene_len = len(gene)
    min_len, n = gene_len, gene_len/4
    left, right = 0,0
    while left < gene_len and right < gene_len:
        if False in [x <= n for x in gene_dic.values()]:
            gene_dic[gene[right]] -= 1
            right += 1
        else:
            min_len = min(min_len, right-left)
            gene_dic[gene[left]] += 1
            left += 1
    return min_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
