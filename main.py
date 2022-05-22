
import datetime as dt
import pandas
import random
import smtplib
my_email = "Aleshichevigor@outlook.com"
password = "45rhfy7853rt"


now = dt.datetime.now()
today_month = now.month
today_day = now.day
today_tuple = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]):
                      data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]  # key today_tuple
    file_path = f"letter_templates\letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_files:
        contents = letter_files.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()     # защита письма
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{contents}")




