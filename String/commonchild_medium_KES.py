import os

def commonChild(s1, s2):
    lgth = len(s1)
    matrix = []

    # Make LCS matrix
    for i in range(lgth + 1):
        matrix.append([])
        for j in range(lgth + 1):
            if i == 0 or j == 0:
                matrix[i].append(0)
            elif s1[i - 1] == s2[j - 1]:
                matrix[i].append(matrix[i - 1][j - 1] + 1)
            elif s1[i - 1] != s2[j - 1]:
                matrix[i].append(max(matrix[i - 1][j], matrix[i][j - 1]))

    return matrix[lgth][lgth]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
