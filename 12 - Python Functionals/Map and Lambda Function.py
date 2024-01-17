cube = lambda x: x**3

def fibonacci(n):
    if(n == 0): return []
    prev = 0
    secprev = 1
    res = [0]
    for _ in range(n-1):
        curr = prev+secprev
        res.append(curr)
        secprev = prev
        prev = curr
    return res

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))