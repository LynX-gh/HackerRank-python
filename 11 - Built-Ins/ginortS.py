if __name__ == '__main__':
    arr = sorted(input())
    low = filter(lambda x: x.islower(), arr)
    up = filter(lambda x: x.isupper(), arr)
    even = filter(lambda x: (x.isnumeric()) and (int(x) % 2 == 0), arr)
    odd = filter(lambda x: (x.isnumeric()) and (int(x) % 2 == 1), arr)
    print(*low, *up, *odd, *even, sep='')
