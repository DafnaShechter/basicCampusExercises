import datetime
import calendar

date_string = input("Enter a date (dd/mm/yyyy): ")
day, month, year = map(int, date_string.split('/'))

weekday_num = datetime.date(year, month, day).weekday()
weekday_name = calendar.day_name[weekday_num]

print(weekday_name)
