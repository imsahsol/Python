from datetime import datetime

birthday = datetime(1998, 4, 23, 10, 50, 12)

print(birthday.year)
print(birthday.weekday())
print(datetime.now())
print(datetime(2018, 1, 1) - datetime(2017, 1, 1))
print(datetime.now() - datetime(2018,1,1))

parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
print(parsed_date)
print(parsed_date.month)
print(parsed_date.weekday())
print(parsed_date.year)

date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)