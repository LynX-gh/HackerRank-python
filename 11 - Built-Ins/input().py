if __name__ == '__main__':
    x, res = map(int, input().split(' '))
    eqn = input()
    print(eval(eqn) == res)