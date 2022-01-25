n, m = map(int, input().split())
arr = map(int, input().split())
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

happy = 0

for i in arr:
    if i in set1:
       happy += 1
    elif i in set2:
        happy -= 1

print(happy)