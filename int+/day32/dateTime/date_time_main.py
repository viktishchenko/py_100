# import datetime
import datetime as dt

now = dt.datetime.now() # now>>> 2025-08-12 11:43:14.925417
year = now.year # now>>> 2025
month = now.month #>>> 8
day_of_week = now.weekday()
print(f'day_of_week>>> {day_of_week}') # day_of_week>>> 1 0-Mon,1-Tue ...

date_of_birth = dt.datetime(year=1980,month=7,day=19,hour=18,minute=43,second=12) # date_of_birth>>> 1980-07-19 18:43:12
print(f'date_of_birth>>> {date_of_birth}')