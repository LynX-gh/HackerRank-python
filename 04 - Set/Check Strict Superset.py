# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A = set(input().split())
for _ in range(int(input())):
    set_B = set(input().split())
    if (set_B.intersection(set_A) != set_B) or (set_A < set_B) :
        print('False');
        exit()
print('True')
