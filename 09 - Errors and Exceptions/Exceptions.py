if __name__ == '__main__':
    for _ in range(int(input())):
        try:
            x, y = list(map(int, input().split(' ')))
            print(x//y)
        except Exception as e:
            print(f"Error Code: {e}")
