import os
import calendar
import datetime


def validate_date(year, month, day):
    try:
        datetime.datetime(year, month, int(day))
        success = True
    except ValueError:
        success = False
    return success

today = datetime.date.today()
year, month = today.year, today.month

while True:
    os.system('clear')
    print(calendar.month(year, month))

    options = 'j,k,d,q,?\n\n'
    match input(options)[0]:
        case 'j':
            month += 1
            if month > 12:
                month = 1
                year += 1
        case 'k':
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        case 'd':
            date_valid = False
            while not date_valid:
                day = input('Enter day: ')
                date_valid = validate_date(year, month, day)
            print(f'Booking day: {day}/{month}/{year}')
            break
        case 'q':
            break
