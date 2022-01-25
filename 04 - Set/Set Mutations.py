a = int(input())
set_a = set(map(int, input().split()))
nc = int(input())

for i in range(nc):
    command, m = input().split(' ')
    set_m = set(map(int, input().split()))
    getattr(set_a, command)(set_m)
    
print(sum(set_a))