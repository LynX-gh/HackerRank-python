n = int(input())
temp = input().split()
set_A = set(map(int, temp))
m = int(input())
temp = input().split()
set_B = set(map(int, temp))

ans1 = set_A.difference(set_B)
ans2 = set_B.difference(set_A)
ans = ans1.union(ans2)
for i in sorted(ans):
    print(i)