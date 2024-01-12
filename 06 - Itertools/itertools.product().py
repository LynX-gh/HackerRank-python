# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(*list(product(arr1, arr2)))
