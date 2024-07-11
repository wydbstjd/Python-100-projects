import smtplib
import datetime as dt
import random

MY_EMAIL = "'''" # enter your email
MY_PASSWORD = "'''" # enter your password

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("./quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Monday Motivation\n\n{quote}")

# UnicodeEncodeError: 'ascii' codec can't encode characters in position 5-7: ordinal not in range(128) 에러 발생