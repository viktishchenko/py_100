

from datetime import datetime


# today = datetime.date.today() # 2025-09-03
# now_time = today.strftime("%X") # 

today_date = datetime.now().strftime("%d/%m/%Y") # 03/09/2025
now_time = datetime.now().strftime("%X") # 09:22:21
current_time = datetime.now().time() # 09:25:00.881544

# print(f'today_date>>> {today_date}')
# print(f'now_time>>> {now_time}')
print(f'current_time>>> {current_time}')
