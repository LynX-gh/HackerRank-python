if __name__ == '__main__':
    marks = []
    n = int(input())
    i = input().split().index('MARKS')
    for _ in range(n):
        marks.append(int(input().split()[i]))
    print(sum(marks)/n)