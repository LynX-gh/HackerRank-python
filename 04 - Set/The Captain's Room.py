fam = int(input())
room_list = list(map(int, input().strip().split()))
room_single, room_multiple = set(), set()

for room in room_list:
    if room not in room_single:
        room_single.add(room)
    else:
        room_multiple.add(room)

print(room_single.difference(room_multiple).pop())
