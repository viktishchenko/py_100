import time
from datetime import datetime

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

# Новые глобальные переменные для дополнительных функций
SERVICE_PASSWORD = "admin123"
operation_history = []
AUTO_REFILL_THRESHOLD = {
    'water': 100,
    'milk': 50,
    'coffee': 30
}

def log_operation(action, details=""):
    """Логирует все операции машины"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    operation_history.append(f"{timestamp} - {action} {details}")
    # Сохраняем только последние 100 операций
    if len(operation_history) > 100:
        operation_history.pop(0)

def show_history():
    """Показывает историю операций"""
    print("\n" + "="*25)
    print("=== OPERATION HISTORY ===")
    print("="*25)
    for record in operation_history[-10:]:  # Показываем последние 10 операций
        print(record)
    input("\nPress Enter to return to menu...")

def check_auto_refill():
    """Автоматически пополняет ресурсы если они ниже порога"""
    refilled = False
    for resource, threshold in AUTO_REFILL_THRESHOLD.items():
        if resources[resource] < threshold:
            refill_amount = threshold * 3  # Пополняем в 3 раза больше порога
            resources[resource] += refill_amount
            log_operation(f"AUTO-REFILL", f"+{refill_amount} {resource}")
            refilled = True
    if refilled:
        print("\n⚠️ Low resources detected. Auto-refill completed!")
        show_resources()

def service_mode():
    """Режим обслуживания с паролем"""
    print("\n" + "="*25)
    print("=== SERVICE MODE ===")
    print("="*25)
    
    # Проверка пароля
    attempt = input("Enter service password: ")
    if attempt != SERVICE_PASSWORD:
        print("❌ Access denied! Wrong password.")
        log_operation("SECURITY", "Failed login attempt")
        return
    
    log_operation("SERVICE", "Login successful")
    
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
            log_operation("REFILL", f"Water:{water_add}ml Milk:{milk_add}ml Coffee:{coffee_add}g")
            show_resources()
        else:
            print("\n❌ Changes canceled")
            log_operation("SERVICE", "Refill canceled")
    except ValueError:
        print("\n⚠️ Error: Please enter numbers only")
        log_operation("ERROR", "Invalid input in service mode")

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
    print("=== COFFEE MACHINE v2.0 ===")
    print("="*25)
    log_operation("SYSTEM", "Machine started")
    
    while True:
        check_auto_refill()  # Проверка ресурсов перед каждым действием
        
        choice = input("\nMain menu:\n"
                      "1. Order (espresso/latte/cappuccino)\n"
                      "2. Report\n"
                      "3. Service Mode\n"
                      "4. Collect Money\n"
                      "5. Show History\n"  # Новая опция
                      "6. Turn Off\n"
                      "Your choice: ").lower()
        
        if choice == '6' or choice == 'off':
            log_operation("SYSTEM", "Machine stopped")
            print("\nTurning off the machine... Goodbye!")
            break
            
        elif choice == '2' or choice == 'report':
            show_resources()
            
        elif choice == '3' or choice == 'service':
            service_mode()
            
        elif choice == '4' or choice == 'collect':
            collect_money()
            
        elif choice == '5' or choice == 'history':
            show_history()
            
        elif choice in MENU:
            order_process(choice)  # Вынесена в отдельную функцию для удобства
        else:
            print("\n⚠️ Invalid choice. Please try again.")

def order_process(drink):
    """Обрабатывает заказ напитка"""
    missing = check_resources(drink)
    if missing:
        print(f"\n⚠️ Sorry, not enough {', '.join(missing)}.")
        log_operation("ERROR", f"Not enough {', '.join(missing)} for {drink}")
        return
        
    print(f"\nPrice: ${MENU[drink]['cost']:.2f}")
    payment = process_coins()
    
    if payment < MENU[drink]['cost']:
        print("\n❌ Sorry, that's not enough money. Money refunded.")
        log_operation("ORDER", f"{drink} - Payment failed")
    else:
        change = round(payment - MENU[drink]['cost'], 2)
        if change > 0:
            print(f"\nHere's ${change:.2f} in change.")
        resources['money'] += MENU[drink]['cost']
        make_drink(drink)
        log_operation("ORDER", f"Success: {drink} ${MENU[drink]['cost']:.2f}")

# Запуск кофемашины
coffee_machine()