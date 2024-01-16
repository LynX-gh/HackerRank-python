from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    for k, v in Counter(s).most_common(3):
        print(k, v)
