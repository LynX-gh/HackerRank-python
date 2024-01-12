# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == '__main__':
    string, num = input().split(' ')
    res = sorted(list(permutations(string, int(num))))
    for tup in res:
        print(''.join(tup))
