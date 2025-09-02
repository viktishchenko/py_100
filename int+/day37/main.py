import os
from pathlib import Path
from dotenv import load_dotenv
import requests

# Загрузка .env из папки config
current_dir = Path(__file__).parent  # ... day37
env_path = current_dir / 'config' / '.env'

if env_path.exists():
# Загрузка переменных окружения из .env файла
    load_dotenv(dotenv_path=env_path)
    print(f"Загружен .env файл: {env_path}")
else:
    print("Файл .env не найден по пути:", env_path)

ENDPOINT = os.getenv('ENDPOINT')
TOKEN = os.getenv('TOKEN')
USERNAME = os.getenv('USER_NAME')
GRAPH_IDS = ['py100', 'eng']
GRAPH_NAMES = ['py_100', 'english']
GRAPH_UNITS = ['commit', 'hours']


# CREATE USER

# user = requests.post(url=ENDPOINT, json={
#   'token': TOKEN,
#   'username': USER_NAME,
#   'agreeTermsOfService': 'yes',
#   'notMinor': 'yes'
# }) # .text: {"message":"Success. Let's visit https://pixe.la/@vik01 , it is your profile page!","isSuccess":true}

# CREATE GRAPHS

graph_endpoint = f'{ENDPOINT}/{USERNAME}/graphs'
graph_config = {
          'id': F'{GRAPH_IDS[0]}',
          'name': f'{GRAPH_NAMES[0]}',
          'unit': f'{GRAPH_UNITS[0]}',
          'type': 'int',
          'color': 'ajisai',
          'timezone': 'Asia/Bishkek'
          }
graph_headers = {
          'X-USER-TOKEN': TOKEN
          }

# graph = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers) # .text {"message":"This graphID already exist.","isSuccess":false}

# print(f'graph>>> {graph.text}')

# GRAPH PIXEL ADD VALUE
from datetime import date

graph_value_endpoint = f'{ENDPOINT}/{USERNAME}/graphs/{GRAPH_IDS[0]}'
# graph_value_endpoint = f'{ENDPOINT}/{USERNAME}/graphs/{GRAPH_NAMES[1]}'
today = date.today()
# current_day = date.today().strftime('%Y%m%d')
# current_day = ''.join(str(date.today()).split('-'))
graph_value = '2'
graph_value_config = {
    'date': f'{today.year}{today.month:02d}{today.day:02d}',
    'quantity': graph_value,
    'timezone': 'Asia/Bishkek'
}

graph_pixel_add_value = requests.post(url=graph_value_endpoint,json=graph_value_config,headers=graph_headers) # .text {"message":"Success.","isSuccess":true}

print(f'graph_pixel_add_value>>> {graph_pixel_add_value}')

# UPDATE GRAPH
# graph_pixel_update = requests.put(url=graph_value_endpoint,json=graph_config,headers=graph_headers) # .text {"message":"Success.","isSuccess":true}

# print(f'graph_pixel_update.text>>> {graph_pixel_update.text}')

# DELETE GRAPH
# graph_pixel_delete = requests.delete(url=graph_value_endpoint,headers=graph_headers) # .text {"message":"Success.","isSuccess":true}

# print(f'graph_pixel_delete.text>>> {graph_pixel_delete.text}')

