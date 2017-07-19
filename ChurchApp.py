#The ChurchApp
'''
The Church app is a tool that contains a counter that sums up the money for day,
calculates various percentages and  prints the saves the date

also it sums up the total remittances for a particular span of time and prints it

it puts the whole details in a printable format

'''

# Denomination
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
day_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

endings = ['st', 'nd', 'rd'] + ['th'] * 17 + ['st', 'nd', 'rd'] + ['th'] * 7 + ['st']


def date(number, date_type):
    if date_type == 'month':
        if number >= 1 and number <= 12:
            return True
    elif date_type == 'day':
        if number >= 1 and number <= 31:
            return True
    elif date_type == 'year':
        if number >= 2009 and number <= 2017:
            return True
    elif date_type == 'dw':
        if number >= 1 and number <= 7:
            return True
    else:
        return False


while True:
    year = int(input('Year: '))
    year_int = int(year)
    if date(year_int, 'year') is True:
        break
    else:
        print('Wrong input. Try again')

while True:
    month = input('Month(1-12): ')
    month_int = int(month)
    if date(month_int, 'month') is True:
        break
    else:
        print('Wrong input. Try again')

while True:
    day = input('Day(1-31): ')
    day_int = int(day)
    if date(day_int, 'day') is True:
        break
    else:
        print('Wrong input. Try again')
while True:
    dw = input('DOW(1-7): ')
    dw_int = int(dw)
    if date(dw_int, 'dw') is True:
        break
    else:
        print('Wrong input. Try again')

month_number = int(month)
day_number = int(day)
day_of_week_no = int(dw)

day_name = day_of_week[day_of_week_no - 1]
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]






def denom(value):
    if value is int:
        return True
    else:
        return False

while True:
    try:
        five =int(input('₦5: '))

    except ValueError:
        print('Invalid input. Please try again')
    else:
        break
while True:
    try:
        ten = int(input('₦10: '))
    except ValueError:
        print('Invalid input. Please try agsin')
    else:
        break
while True:
    try:
        twenty = int(input('₦20: '))
    except ValueError:
        print('Invalid input. Please try agsin')
    else:
        break

while True:
    try:
        fifty = int(input('₦50: '))
    except ValueError:
        print('Invalid input. Please try agsin')
    else:
        break
while True:
    try:
        one_hundred = int(input('₦100: '))
    except ValueError:
        print('Invalid input. Please try agsin')
    else:
        break
while True:
    try:
        two_hundred = int(input('₦200: '))
    except ValueError:
        print('Invalid input. Please try agsin')
    else:
        break
while True:
        try:
            five_hundred = int(input('₦500: '))
        except ValueError:
            print('Invalid input. Please try agsin')
        else:
            break
while True:
    try:
        one_thousand = int(input('₦1000: '))
    except ValueError:
        print('Invalid input. Please try agsin')
    else:
        break

amount_five = 5 * five
amout_ten = 10 * ten
amount_twenty = 20 * twenty
amount_fifty = 50 * fifty
amount_one_hundred = 100 * one_hundred
amount_two_hundred = 200 * two_hundred
amount_five_hundred = 500 * five_hundred
amount_one_thousand = 1000 * one_thousand

total = amount_five + amout_ten + amount_twenty + amount_fifty + amount_one_hundred + amount_two_hundred + amount_five_hundred + amount_one_thousand

from decimal import Decimal as D
while True:
    monetary = input(
        "What monetary is this? Minister's Tithe(mt), Member's Tithe(t),Thanksgiving(tg),\n SeedLoveOffering(slo)"
        "CRM(crm), Gospel Fund(gf), FirstFrruit(ff)")
    if monetary == 'mt':
        offering_remitance = D(0.775 * total)
        remitance = D(round(offering_remitance, 2))
        print("The total Minister's Tithe for today is ₦", total)
        print("Minister's Tithe remitance for today is ₦", remitance)
        break

    elif monetary == 't':
        offering_remitance = D(0.7 * total)
        remitance = D(round(offering_remitance, 2))
        print("The total Member's Tithe for today is ₦", total)
        print("Member's Tithe remitance for today is ₦", remitance)
        break
    elif monetary == "tg":
        offering_remitance = D(0.7 * total)
        remitance = D(round(offering_remitance, 2))

        print("The total Thanksgiving for today is ₦", total)
        print("Thanksgiving remitance for today is ₦", remitance)
    elif monetary == 'slo':
        offering_remitance = D(0.3 * total)
        remitance = D(round(offering_remitance, 2))
        print("The total SLO for today is ₦", total)
        print("SLO remitance for today is ₦", remitance)
        break
    elif monetary == 'crm':
        offering_remitance = D(0.5 * total)
        remitance = D(round(offering_remitance, 2))
        print("The total CRM for today is ₦", total)
        print("CRM remitance for today is ₦", remitance)
        break
    elif monetary == 'gf':
        offering_remitance = D(0.25 * total)
        remitance = D(round(offering_remitance, 2))
        print("The Gospel Fund for today is ₦", total)
        print("Gospel Fund remitance for today is ₦", remitance)
        break
    elif monetary == 'ff':
        offering_remitance = D(0.1 * total)
        remitance = D(round(offering_remitance, 2))
        print("The total First Fruuit for today is ₦", total)
        print("First Fruit remitance for today is ₦", remitance)
        break
    else:
        print("Invalid input. Please try again")
        continue


print(day_name + ", " + month_name + ' ' + ordinal + ',', year)