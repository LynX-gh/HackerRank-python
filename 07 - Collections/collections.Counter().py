from collections import Counter

if __name__ == '__main__':
    res = 0
    _ = input()
    shoeCtr = Counter(list(map(int, input().split(' '))))
    for _ in range(int(input())):
        size, price = list(map(int, input().split(' ')))
        if shoeCtr[size]:
            shoeCtr[size]-=1
            res+=price
    print(res)