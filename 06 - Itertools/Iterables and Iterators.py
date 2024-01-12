# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

def _internal(tup):
    if 'a' in tup:
        return True
    return False

if __name__ == '__main__':
    x = int(input())
    y = input().split(' ')
    z = int(input())
    resArr = list(itertools.combinations(y, z))
    resDen = len(resArr)
    resNum = len(list(filter(_internal, resArr)))
    print(resNum/resDen)
