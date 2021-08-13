def minion_game(string):
    stuart = 0
    kevin = 0
    vowels = 'AEIOU'
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string)-i
        else:
            stuart += len(string)-i

    if kevin > stuart:
        print("Kevin {}".format(kevin))
    elif stuart > kevin:
        print("Stuart {}".format(stuart))
    else:
        print("Draw")