# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

if __name__ == '__main__':
    sample = input()
    for (k, r) in groupby(sample):
        print(f'({len(list(r))}, {k})', end=' ')
