import datetime as dt
import smtplib
import random

MY_EMAIL = 'myrealmailaddress@gmail.com'
PSWRD = 'qwewqdsfcxvsf'
SEND_TO ='emailtosendaddress@yahoo.com'


# GET QUOTE
def get_quote():
  try:
    with open('int+/day32/quotes.txt') as file:
      # text = file.read()
      # # OR______________
      quotes_arr = file.readlines()
      # print(f'len(quotes_arr)>>> {len(quotes_arr)}') # 102
      # print(f'len(quotes_arr)>>> {quotes_arr[1]}') # "Either y.. you." - Jim Rohn
  except FileNotFoundError as msg_error:
    print(f'Quotes not found: {msg_error}')
  else:
      # quotes_arr = text.split('\n')
      random_quote = random.choice(quotes_arr)
      return random_quote
  finally:
    pass

# GET CURRENT DAY SEND EMAIL
now = dt.datetime.now() # now>>> 2025-08-12 11:43:14.925417
weekday = now.weekday()
if weekday == 2:
  quote = get_quote()
  print(f'quote>>> {quote}')
with smtplib.SMTP('smtp.gmail.com') as connection:
  connection.starttls()
  connection.login(user=MY_EMAIL, password=PSWRD)
  connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=SEND_TO,
    msg=f'sUBJECT: Tuesday MOTIVATION quote!\n\n{quote}'
  )


