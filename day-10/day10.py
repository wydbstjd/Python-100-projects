# def format_name(f_name, l_name):
#     if f_name == '' or l_name == '':
#         return "You didn't provide valid inputs"
    
#     f_name = f_name.title()
#     l_name = l_name.title()

#     return f"{f_name} {l_name}"

# print(format_name(input('What is your first name? '), input('What is your last name? ')))


# def is_leap(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print("Leap year")
#         return True
    
#     else:
#         print('Not Lear year, ', end='')
#         return False

# def is_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#     if month == 2 and is_leap(year):
#         return 29
    
#     else:
#         return month_days[month-1]
    
# year = int(input('year? '))
# month = int(input("month? "))

# days = is_month(year, month)
# print(days)


from replit import clear
from art import logo3

def cal(a, mark, b):
    if mark == '+':
        return a+b
    elif mark == '-':
        return a-b
    elif mark == '*':
        return a*b
    else:
        return a/b
    
print(logo3)

again = True

while (True):
    if again == True or again == 'n':
        first_num = float(input("What's the first number?: "))
        print("+\n-\n*\n/")

    mark = input("Pick an operation: ")
    last_num = float(input("What's the next number?: "))
    result = cal(first_num,mark,last_num)
    print(f'{first_num} {mark} {last_num} = {result}')
    again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")

    if again == 'y':
        first_num = result

    else:
        clear()