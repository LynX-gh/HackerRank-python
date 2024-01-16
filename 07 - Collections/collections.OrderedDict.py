from collections import defaultdict

if __name__ == '__main__':
    res = defaultdict(lambda: 0)
    n = int(input())
    for _ in range(n):
        line = input().split()
        res[' '.join(line[:-1])] += int(line[-1])
    for k, v in res.items():
        print(k, v)
