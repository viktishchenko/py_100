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

def show_resources():
    """Показывает текущий уровень ресурсов"""
    print("\n=== CURRENT RESOURCES ===")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}\n")

def service_mode():
    """Режим обслуживания с защитой от некорректного ввода"""
    print("\n" + "="*25)
    print("=== SERVICE MODE ===")
    print("="*25)
    
    try:
        water_add = max(0, int(input("Enter water to add (ml): ") or 0))
        milk_add = max(0, int(input("Enter milk to add (ml): ") or 0))
        coffee_add = max(0, int(input("Enter coffee to add (g): ") or 0))
        
        print("\nChanges to be made:")
        print(f"+ {water_add}ml Water")
        print(f"+ {milk_add}ml Milk")
        print(f"+ {coffee_add}g Coffee")
        
        confirm = input("\nConfirm changes? (y/n): ").lower()
        if confirm == 'y':
            resources['water'] += water_add
            resources['milk'] += milk_add
            resources['coffee'] += coffee_add
            print("\n✅ Resources updated successfully!")
            show_resources()
        else:
            print("\n❌ Changes canceled")
    except ValueError:
        print("\n⚠️ Error: Please enter numbers only")

def check_resources(drink):
    """Проверяет достаточно ли ингредиентов для напитка"""
    missing = []
    for ingredient, amount in MENU[drink]['ingredients'].items():
        if resources[ingredient] < amount:
            missing.append(ingredient)
    return missing if missing else None

def process_coins():
    """Обрабатывает ввод монет с защитой от ошибок"""
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
                if count < 0:
                    print("Please enter positive numbers!")
                    continue
                total += count * value
                break
            except ValueError:
                print("Please enter numbers only!")
    return round(total, 2)

def make_drink(drink):
    """Готовит напиток и обновляет ресурсы"""
    for ingredient, amount in MENU[drink]['ingredients'].items():
        resources[ingredient] -= amount
    print(f"\nHere's your {drink} ☕. Enjoy!")

def collect_money():
    """Функция сбора денег из аппарата"""
    print("\n" + "="*25)
    print(f"💵 Current balance: ${resources['money']:.2f}")
    amount = float(input("Enter amount to collect: $"))
    if 0 < amount <= resources['money']:
        resources['money'] -= amount
        print(f"✅ Collected ${amount:.2f}")
        print(f"Remaining balance: ${resources['money']:.2f}")
    else:
        print("❌ Invalid amount!")

def coffee_machine():
    print("\n" + "="*25)
    print("=== COFFEE MACHINE ===")
    print("="*25)
    
    while True:
        choice = input("\nMain menu:\n"
                      "1. Order (espresso/latte/cappuccino)\n"
                      "2. Report\n"
                      "3. Service Mode\n"
                      "4. Collect Money\n"
                      "5. Turn Off\n"
                      "Your choice: ").lower()
        
        if choice == '5' or choice == 'off':
            print("\nTurning off the machine... Goodbye!")
            break
            
        elif choice == '2' or choice == 'report':
            show_resources()
            
        elif choice == '3' or choice == 'service':
            service_mode()
            
        elif choice == '4' or choice == 'collect':
            collect_money()
            
        elif choice in MENU:
            missing = check_resources(choice)
            if missing:
                print(f"\n⚠️ Sorry, not enough {', '.join(missing)}.")
                continue
                
            print(f"\nPrice: ${MENU[choice]['cost']:.2f}")
            payment = process_coins()
            
            if payment < MENU[choice]['cost']:
                print("\n❌ Sorry, that's not enough money. Money refunded.")
            else:
                change = round(payment - MENU[choice]['cost'], 2)
                if change > 0:
                    print(f"\nHere's ${change:.2f} in change.")
                resources['money'] += MENU[choice]['cost']
                make_drink(choice)
        else:
            print("\n⚠️ Invalid choice. Please try again.")

# Запуск кофемашины
coffee_machine()