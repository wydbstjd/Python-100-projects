def check_amount(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}')
            return False
        return True

def check_coin(name):
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))

    coin = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    balance = coin - MENU[name]['cost']
    if balance >= 0:

        resources['water'] -= MENU[name]['ingredients']['water']
        resources['coffee'] -= MENU[name]['ingredients']['coffee']
        if name == 'latte' or name == 'cappuccino':
            resources['milk'] -= MENU[name]['ingredients']['milk']

        return balance
    else:
        return "Sorry that's not enough money. Money refunded."

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
is_on = True
while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        is_on = False

    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice]
        check = check_amount(drink['ingredients'])
        if check:
            change = check_coin(choice)
            if isinstance(change,float):
                print(f"Here is ${change:.2f} in change.")
                print(f'Here is your {choice}. Enjoy!')
                profit += MENU[choice]['cost']
            else:
                print(change)