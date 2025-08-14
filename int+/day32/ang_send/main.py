from datetime import datetime
import pandas as pd
import random
import smtplib


MY_EMAIL = "exampleemail"
MY_PASSWORD = "password"


today = datetime.now()
today_tuple = (today.month, today.day)
# print(today_tuple) # (8, 14)

data = pd.read_csv("int+/day32/birthdays.csv")
# print(data)
#     name        email      year  month  day
# 0  Peter  peter@email.com  1961     12   21
# 1   John   john@email.com  1997      2   28
# 2  Marta  marta@email.com  1989      8   13


birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(birthdays_dict)
      # name               Peter
      # email    peter@email.com
      # year                1961
      # month                 12
      # day                   21


if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"int+/day32/letter_templates/etter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )