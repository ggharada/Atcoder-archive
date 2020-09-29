import datetime
y,m,d = map(int,input().split("/"))
d = datetime.datetime(y,m,d)

while d.year % d.month != 0 or d.year // d.month % d.day != 0:
    d += datetime.timedelta(days = 1)
print(d.strftime("%Y/%m/%d"))