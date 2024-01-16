from collections import deque

if __name__ == '__main__':
    q = deque()
    for _ in range(int(input())):
        method, *args = input().split()
        getattr(q, method)(*args)
    print(*q)
