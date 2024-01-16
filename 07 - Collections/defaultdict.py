from collections import defaultdict

if __name__ == '__main__':
    n, m = list(map(int, input().split(' ')))
    grp1 = defaultdict(lambda: [])
    
    for i in range(n):
        grp1[input()].append(i+1)
    for _ in range(m):
        temp = input()
        print(*grp1[temp]) if grp1[temp] else print(-1)
