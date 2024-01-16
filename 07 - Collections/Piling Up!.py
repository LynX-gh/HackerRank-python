# Enter your code here. Read input from STDIN. Print output to STDOUT
def piling_up(arr: list) -> str:
    lptr = 1
    rptr = len(arr)-2
    lastMax = max(arr[0], arr[-1])
    while lptr <= rptr:
        if max(arr[lptr], arr[rptr]) > lastMax:
            return "No"
        lastMax = max(arr[lptr], arr[rptr])
        lptr += 1
        rptr -= 1
    return "Yes"

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split(' ')))
        print(piling_up(arr))