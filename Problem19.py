import calendar

counter = 0
cal = calendar.Calendar()
for year in xrange(1901, 2001):
    for month in range(1, 13):
        if cal.monthdayscalendar(year, month)[0][6] == 1:
            counter += 1
print counter
