import re

if __name__ == '__main__':
    num_valid = re.compile(r'([+-]?[0-9]+\.[0-9]+)|([+-]?\.[0-9]+)')
    for _ in range(int(input())):
        print(bool(re.fullmatch(num_valid, input())))
