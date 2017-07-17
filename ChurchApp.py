#The ChurchApp
'''
The Church app is a tool that contains a counter that sums up the money for day,
calculates various percentages and  prints the saves the date

also it sums up the total remittances for a particular span of time and prints it

it puts the whole details in a printable format



'''

# OFFERINGS AND TIHES SETTLERS
# OFFERINGS
# Denomination

five = input('₦5: ')
ten = input('₦10: ')

twenty = input('₦20: ')
fifty = input('₦50: ')
one_hundred = input('₦100: ')
two_hundred = input('₦200: ')
five_hundred = input('₦500: ')
one_thousand = input('₦1000: ')

int_five = int(five)
int_ten = int(ten)
int_twenty = int(twenty)
int_fifty = int(fifty)
int_one_hundred = int(one_hundred)
int_two_hundred = int(two_hundred)
int_five_hundred = int(five_hundred)
int_one_thousand = int(one_thousand)

amount_five = 5 * int_five
amout_ten = 10 * int_ten
amount_twenty = 20 * int_twenty
amount_fifty = 50 * int_fifty
amount_one_hundred = 100 * int_one_hundred
amount_two_hundred = 200 * int_two_hundred
amount_five_hundred = 500 * int_five_hundred
amount_one_thousand = 1000 * int_one_thousand

total = amount_five + amout_ten + amount_twenty + amount_fifty + amount_one_hundred + amount_two_hundred + amount_five_hundred + amount_one_thousand

offering_remitance = 0.1 * total
remitance = round(offering_remitance, 3)
remitance_int = int(remitance)
remitance_str = str(remitance_int)

str_total = str(total)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
day_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

endings = ['st', 'nd', 'rd'] + ['th'] * 17 + ['st', 'nd', 'rd'] + ['th'] * 7 + ['st']


def date(number, date_type):
    if date_type == 'month':
        if number >= 1 and number <= 12:
            return True
    elif date_type == 'day':
        if number >= 1 and number <= 7:
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

print(day_name + ", " + month_name + ' ' + ordinal + ',', year)
print('The total offering/Tithe/FirstFruit/CRM/TG for today is ₦' + str_total)
print('Remitance for today is ₦' + remitance_str)

