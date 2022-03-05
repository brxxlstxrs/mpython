from datetime import datetime, timedelta

date = datetime(2019, 9, 1) + timedelta(int(input()))
print(date.day, date.month)
