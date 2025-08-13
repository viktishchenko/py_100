import csv
import datetime as dt
import random
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv  # py -m pip install python-dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

DIRECTORY_PATH = os.path.join('int+','day32', 'letter_templates')
MY_EMAIL = os.getenv('EMAIL_USER')  # В .env файле: EMAIL_USER=your@email.com
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SEND_TO = os.getenv('EMAIL_TO')

def send_letter(title, letter):
    print(f'title>>> {title} | letter>>> {letter}')
    try:
        msg = EmailMessage()
        msg['Subject'] = title
        msg['From'] = MY_EMAIL
        msg['To'] = SEND_TO
        msg.set_content(letter)

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, EMAIL_PASSWORD)
            connection.send_message(msg)
    except Exception as err:
        print(f'Error sending email: {err}')

def count_letter_templates(path):
    try:
        return len([f for f in os.listdir(path) if f.startswith('letter_') and f.endswith('.txt')])
    except FileNotFoundError:
        print(f"Directory not found: {path}")
        return 0

def prepare_letter(name):
    num_templates = count_letter_templates(DIRECTORY_PATH)
    if not num_templates:
        print("No letter templates found")
        return

    random_letter_num = random.randint(1, num_templates)
    letter_path = os.path.join(DIRECTORY_PATH, f'letter_{random_letter_num}.txt')

    try:
        with open(letter_path, 'r') as file:
            lines = file.readlines()
            if not lines:
                print(f"Empty letter template: {letter_path}")
                return

            letter_greet = lines[0].replace('[NAME]', name.strip())
            letter_msg = ''.join(lines[1:]) if len(lines) > 1 else ""
            personalized_letter = f"{letter_greet}\n{letter_msg}"
            
            title = letter_greet.replace(',', '!').strip()
            send_letter(title, personalized_letter)
    except Exception as err:
        print(f'Error creating email for {name}: {err}')

def check_birthdays():
    try:
        with open(os.path.join('int+', 'day32', 'birthdays.csv'), 'r') as file:
            dict_reader = csv.DictReader(file)
            today = dt.datetime.now()
            for row in dict_reader:
                if int(row['month']) == today.month and int(row['day']) == today.day:
                    prepare_letter(row['name'])
    except FileNotFoundError as error_msg:
        print(f'Birthday list not found: {error_msg}')
    except Exception as error_msg:
        print(f'Error processing birthdays: {error_msg}')

if __name__ == "__main__":
    check_birthdays()