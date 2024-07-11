##################### Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL = "'''" # enter your email
MY_PASSWORD = "'''" # enter your password

today = (dt.datetime.now().month, dt.datetime.now().day)
data = pd.read_csv("./birthdays.csv")

birthdays_dict = {(row.month,row.day): row for (index, row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, "r") as letter_file:
        data = letter_file.read()
        data.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person['email'], msg=f"Subject: Happy Birthday!\n\n{data}")
