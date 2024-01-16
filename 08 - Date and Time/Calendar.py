import calendar

mm, dd, yyyy = list(map(int, input().split(' ')))
day = calendar.weekday(yyyy, mm, dd)
print(calendar.day_name[day].upper())
