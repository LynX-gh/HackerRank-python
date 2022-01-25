# Enter your code here. Read input from STDIN. Print output to STDOUT
cases = int(input())
for _ in range(cases):
    n, set_n = input(), set(map(int, input().split()))
    m, set_m = input(), set(map(int, input().split()))
    if set_m.intersection(set_n) == set_n:
        print('True');
    else:
        print('False')