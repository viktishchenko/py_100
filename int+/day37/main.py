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

CTREAT_ENDPOINT = os.getenv('CREATE_ENDPOINT')
TOKEN = os.getenv('TOKEN')
USERNAME = os.getenv('USER_NAME')
print(f'USER_NAME>>> {USERNAME}')


# CREATE USER

# user = requests.post(url=ENDPOINT, json={
#   'token': TOKEN,
#   'username': USER_NAME,
#   'agreeTermsOfService': 'yes',
#   'notMinor': 'yes'
# }) # .text: {"message":"Success. Let's visit https://pixe.la/@vik01 , it is your profile page!","isSuccess":true}

# CREATE GRAPHS

graph_endpoint = f'{CTREAT_ENDPOINT}/{USERNAME}/graphs'
graph_config = {
          'id': 'py100',
          'name': 'py100',
          'unit': 'commit',
          'type': 'int',
          'color': 'ajisai'
          }
graph_headers = {
          'X-USER-TOKEN': TOKEN
          }

graph = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers) # .text {"message":"This graphID already exist.","isSuccess":false}