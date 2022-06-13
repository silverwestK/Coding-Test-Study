import os

def pangrams(s):
    s = set(s.replace(' ', '').lower())
    return 'pangram' if len(s) == 26 else 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
