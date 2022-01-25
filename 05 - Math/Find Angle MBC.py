import math

side_A = int(input().strip())
side_B = int(input().strip())
side_C = math.sqrt(side_A**2 + side_B**2)
res=round(math.degrees(math.acos(side_B/side_C)))
print('{}{}'.format(res, chr(176)))
