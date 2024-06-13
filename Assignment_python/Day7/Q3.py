 # 3. Write a python program to print the no. of days to reach your birthday from today

from datetime import datetime

def ip():
    birth_month = int(input("Enter your birth month: "))
    birth_day = int(input("Enter your birth day: "))
    result = days_until_birthday(birth_month, birth_day)
    print(result)

def days_until_birthday(birth_month, birth_day):
    today = datetime.now()
    birthday_this_year = datetime(today.year, birth_month, birth_day)
    if today > birthday_this_year:
        birthday_this_year = datetime(today.year + 1, birth_month, birth_day)
    days_until = (birthday_this_year - today).days
    return f"Days until your next birthday: {days_until}"

ip()
