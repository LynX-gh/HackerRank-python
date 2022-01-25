n = int(input())
set_n = set(map(int, input().split()))
m = int(input())
set_m = set(map(int, input().split()))

print(len(set_n.symmetric_difference(set_m)))