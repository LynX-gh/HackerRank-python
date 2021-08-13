if __name__ == '__main__':
    N = int(input())
    arr = []
    func = []
    for i in range(N):
        func = input().strip().split()
        if len(func) == 1:
            if(func[0] == 'print'):
                print(arr)
            else:
                getattr(arr, func[0])()
        elif len(func) == 2:
            getattr(arr, func[0])(int(func[1]))
        elif len(func) == 3:
            getattr(arr, func[0])(int(func[1]), int(func[2]))