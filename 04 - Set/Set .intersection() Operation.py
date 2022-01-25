nE = int(input().strip())
set_nE = set(map(int, input().strip().split()))
nF = int(input().strip())
set_nF = set(map(int, input().strip().split()))

un_nEnF = set_nE.intersection(set_nF)
print(len(un_nEnF))
