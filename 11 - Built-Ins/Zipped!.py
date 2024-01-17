if __name__ == '__main__':
    n, x = map(int, input().split(' '))
    marks = []
    for _ in range(x):
        marks.append(list(map(float, input().split(' '))))
    for tup in zip(*marks):
        print(sum(tup) / x)
