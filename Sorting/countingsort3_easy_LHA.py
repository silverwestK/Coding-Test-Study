import os

def countingSort():
    frequency = [0] * 100
    starting_values = [0] * 100
    n_list = []
    n = int(input().strip())

    for i in range(n):
        k = input().split()[0]
        n_list.append(k)

    for i in n_list:
        frequency[int(i)] += 1

    for i in range(100):
        starting_values[i] = sum(frequency[:i + 1])

    return starting_values

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = countingSort()

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
