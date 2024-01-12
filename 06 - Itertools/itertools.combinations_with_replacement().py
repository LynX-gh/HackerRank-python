# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == '__main__':
    string, num = input().split(' ')
    res = combinations_with_replacement(sorted(string), int(num))
    for tup in res:
        print(''.join(tup))
