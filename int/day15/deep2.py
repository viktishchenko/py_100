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

def service_mode():
    """Режим обслуживания для пополнения ресурсов"""
    print("\n=== SERVICE MODE ===")
    resources['water'] += int(input("Enter water to add (ml): ") or 0)
    resources['milk'] += int(input("Enter milk to add (ml): ") or 0)
    resources['coffee'] += int(input("Enter coffee to add (g): ") or 0)
    print("Resources updated successfully!")
    print(f"Current levels - Water: {resources['water']}ml, Milk: {resources['milk']}ml, Coffee: {resources['coffee']}g\n")

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
                count = int(input(f"How many {coin}?: ") or 0)
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
        choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        
        if choice == 'off':
            print("Turning off the machine...")
            break
        elif choice == 'report':
            print(f"\nWater: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']:.2f}\n")
        elif choice == 'service':
            service_mode()
        elif choice in MENU:
            missing = check_resources(choice)
            if missing:
                print(f"Sorry, not enough {', '.join(missing)}.")
                continue
                
            print(f"Price: ${MENU[choice]['cost']:.2f}")
            payment = process_coins()
            
            if payment < MENU[choice]['cost']:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = round(payment - MENU[choice]['cost'], 2)
                if change > 0:
                    print(f"Here's ${change:.2f} in change.")
                resources['money'] += MENU[choice]['cost']
                make_drink(choice)
        else:
            print("Invalid choice. Please try again.")

# Запуск кофемашины
print("=== Coffee Machine ===")
coffee_machine()