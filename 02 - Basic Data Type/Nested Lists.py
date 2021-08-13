if __name__ == '__main__':
    score_record = []
    record = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name, score])
        score_record.append(score)
        
    n = sorted(set(score_record))[1]
    name_record = [x for[x, y] in record if y == n]
    for name in sorted(name_record):
        print(name)