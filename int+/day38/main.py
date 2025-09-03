from datetime import datetime
import os
from dotenv import load_dotenv
import requests

# # Загрузка .env из папки config
# current_dir = Path(__file__).parent  # ... day37
# env_path = current_dir / 'config' / '.env'

# if env_path.exists():
# # Загрузка переменных окружения из .env файла
#     load_dotenv(dotenv_path=env_path)
#     print(f"Загружен .env файл: {env_path}")
# else:
#     print("Файл .env не найден по пути:", env_path)

load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
GENDER = "Male"
AGE = "20"
WEIGHT_KG = "65"
HEIGHT_CM = "175"
TOKEN = os.getenv('TOKEN')

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

print(f'result>>> {result}')

# {'exercises': [{'tag_id': 317, 'user_input': 'run', 'duration_min': 31.08, 'met': 9.8, 'nf_calories': 329.97, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}]}

# {'exercises': [{'tag_id': 187, 'user_input': 'jump', 'duration_min': 15, 'met': 3.5, 'nf_calories': 56.88, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/187_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/187_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 15700, 'name': 'trampoline', 'description': None, 'benefits': None}]}

# {'exercises': [{'tag_id': 317, 'user_input': 'run', 'duration_min': 31.08, 'met': 9.8, 'nf_calories': 329.97, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}, {'tag_id': 187, 'user_input': 'jump', 'duration_min': 15, 'met': 3.5, 'nf_calories': 56.88, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/187_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/187_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 15700, 'name': 'trampoline', 'description': None, 'benefits': None}]}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_endpoint = "https://api.sheety.co/6f3f1d7d2037bdb6ca86fa889e9ef043/copyOfMyWorkouts/workouts"

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

#No Authentication  
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

# {
#   "errors": [
#     {
#       "detail": "Unathorized. A valid 'Authorization' header is required to access this API."
#     }
#   ]
# }


#Basic Authentication
# sheet_response = requests.post(
#   sheet_endpoint, 
#   json=sheet_inputs, 
#   auth=(
#       YOUR USERNAME, 
#       YOUR PASSWORD,
#   )
# )

#Bearer Token Authentication
bearer_headers = {
"Authorization": f"Bearer {TOKEN}"
}

sheet_response = requests.post(
    sheet_endpoint, 
    json=sheet_inputs, 
    headers=bearer_headers
)

print(f'sheet_response.text>>> {sheet_response.text}')

# {
#   "errors": [
#     {
#       "detail": "Unathorized. A valid 'Authorization' header is required to access this API."
#     }
#   ]
# }


