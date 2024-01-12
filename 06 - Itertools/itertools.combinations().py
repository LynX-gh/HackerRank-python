# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    string, num = input().split(' ')
    for i in range(1, int(num)+1):
        res = combinations(sorted(string), i)
        for tup in res:
            print(''.join(tup))
