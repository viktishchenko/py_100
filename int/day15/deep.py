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
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0.0
}

def check_resources(drink):
    """Проверяет достаточно ли ингредиентов для напитка"""
    missing = []
    for ingredient, amount in MENU[drink]['ingredients'].items():
        if resources[ingredient] < amount:
            missing.append(ingredient)
    return missing if missing else None

def process_coins():
    """Обрабатывает ввод монет"""
    coins = {
        'quarters': 0.25,
        'dimes': 0.10,
        'nickles': 0.05,
        'pennies': 0.01
    }
    total = 0.0
    for coin, value in coins.items():
        while True:
            try:
                count = int(input(f"How many {coin}?: "))
                total += count * value
                break
            except ValueError:
                print("Please enter a number!")
    return round(total, 2)

def make_drink(drink):
    """Готовит напиток и обновляет ресурсы"""
    for ingredient, amount in MENU[drink]['ingredients'].items():
        resources[ingredient] -= amount
    print(f"Here's your {drink} ☕. Enjoy!")

def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        
        if choice == 'off':
            break
        elif choice == 'report':
            print(f"\nWater: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}\n")
        elif choice in MENU:
            missing = check_resources(choice)
            if missing:
                print(f"Sorry, not enough {', '.join(missing)}.")
                continue
                
            print(f"Price: ${MENU[choice]['cost']}")
            payment = process_coins()
            
            if payment < MENU[choice]['cost']:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = round(payment - MENU[choice]['cost'], 2)
                if change > 0:
                    print(f"Here's ${change} in change.")
                resources['money'] += MENU[choice]['cost']
                make_drink(choice)
        else:
            print("Invalid choice. Please try again.")

coffee_machine()