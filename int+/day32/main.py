##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import csv
import datetime as dt
import random
import os
import smtplib

DIRECTORY_PATH = 'int+/day32/letter_templates'
MY_EMAIL = 'myemailaddress@gmail.com'
PSWRD = 'qqwerty123'
SEND_TO = 'emailtosendaddress@yahoo.com'

def send_letter(title,letter):
  try:
    with smtplib.SMTP('smtp.gmail.com') as connection:
      connection.starttls()
      connection.login(user=MY_EMAIL, password=PSWRD)
      connection.sendmail(
      from_addr=MY_EMAIL,
      to_addrs= SEND_TO,
      msg=f'Subject:{title}\n\n{letter}'
      )
  except Exception as err:
    print(f'Error send email: {err}')


def count_letter_tmp(path):
  return len(os.listdir(path))

def prepare_letter(n):
  num = count_letter_tmp(DIRECTORY_PATH)
  if num:
    random_letter = random.choice(range(num)) + 1
    try:
      with open(f'int+/day32/letter_templates/letter_{random_letter}.txt', 'r') as letter:
        letter_greet = letter.readline().replace('[NAME]', n)
        letter_msg = (letter.readlines()[1:])
        separator = ""
        result_string = separator.join(letter_msg)
        personalized_letter = f'{letter_greet}\n{result_string}'
    except Exception as err:
      print(f'Error creating email for {n}: {err}')
    else:
      title = letter_greet.replace(',', '!')
      send_letter(title,personalized_letter)


try:
  file = open('int+/day32/birthdays.csv')
  dict_reader = csv.DictReader(file)
except FileNotFoundError as error_msg:
  print(f'Birsday list not found: {error_msg}')
else:
  now = dt.datetime.now()
  month = now.month
  day = now.day
  for row in dict_reader:
    if int(row['month']) == month and int(row['day']) == day:
      prepare_letter(row['name'])
  file.close()





