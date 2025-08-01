import time
from datetime import datetime
from typing import Dict, List, Optional

class CoffeeMachine:
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

    def __init__(self):
        self.resources = {
            'water': 300,
            'milk': 200,
            'coffee': 100,
            'money': 0.0
        }
        self.operation_history = []
        self.SERVICE_PASSWORD = "admin123"
        self.AUTO_REFILL_THRESHOLD = {
            'water': 100,
            'milk': 50,
            'coffee': 30
        }

    def log_operation(self, action: str, details: str = "") -> None:
        """Логирует операцию в историю"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.operation_history.append(f"{timestamp} - {action} {details}")
        if len(self.operation_history) > 100:
            self.operation_history.pop(0)

    def show_resources(self) -> None:
        """Выводит текущий уровень ресурсов"""
        print("\n=== CURRENT RESOURCES ===")
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.resources['money']:.2f}\n")

    def check_resources(self, drink: str) -> Optional[List[str]]:
        """Проверяет достаточно ли ресурсов для напитка"""
        missing = []
        for ingredient, amount in self.MENU[drink]['ingredients'].items():
            if self.resources[ingredient] < amount:
                missing.append(ingredient)
        return missing if missing else None

    def process_coins(self) -> float:
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
                    if count < 0:
                        print("Please enter positive numbers!")
                        continue
                    total += count * value
                    break
                except ValueError:
                    print("Please enter numbers only!")
        return round(total, 2)

    def make_drink(self, drink: str) -> None:
        """Готовит напиток и обновляет ресурсы"""
        for ingredient, amount in self.MENU[drink]['ingredients'].items():
            self.resources[ingredient] -= amount
        print(f"\nHere's your {drink} ☕. Enjoy!")

    def check_auto_refill(self) -> None:
        """Автоматически пополняет ресурсы при необходимости"""
        refilled = False
        for resource, threshold in self.AUTO_REFILL_THRESHOLD.items():
            if self.resources[resource] < threshold:
                refill_amount = threshold * 3
                self.resources[resource] += refill_amount
                self.log_operation("AUTO-REFILL", f"+{refill_amount} {resource}")
                refilled = True
        if refilled:
            print("\n⚠️ Low resources detected. Auto-refill completed!")
            self.show_resources()

    def service_mode(self) -> None:
        """Режим обслуживания с паролем"""
        print("\n" + "="*25)
        print("=== SERVICE MODE ===")
        print("="*25)
        
        if input("Enter service password: ") != self.SERVICE_PASSWORD:
            print("❌ Access denied! Wrong password.")
            self.log_operation("SECURITY", "Failed login attempt")
            return
        
        self.log_operation("SERVICE", "Login successful")
        
        try:
            water_add = max(0, int(input("Enter water to add (ml): ") or 0))
            milk_add = max(0, int(input("Enter milk to add (ml): ") or 0))
            coffee_add = max(0, int(input("Enter coffee to add (g): ") or 0))
            
            print("\nChanges to be made:")
            print(f"+ {water_add}ml Water")
            print(f"+ {milk_add}ml Milk")
            print(f"+ {coffee_add}g Coffee")
            
            if input("\nConfirm changes? (y/n): ").lower() == 'y':
                self.resources['water'] += water_add
                self.resources['milk'] += milk_add
                self.resources['coffee'] += coffee_add
                print("\n✅ Resources updated successfully!")
                self.log_operation("REFILL", f"Water:{water_add}ml Milk:{milk_add}ml Coffee:{coffee_add}g")
                self.show_resources()
            else:
                print("\n❌ Changes canceled")
                self.log_operation("SERVICE", "Refill canceled")
        except ValueError:
            print("\n⚠️ Error: Please enter numbers only")
            self.log_operation("ERROR", "Invalid input in service mode")

    def collect_money(self) -> None:
        """Сбор денег из аппарата"""
        print("\n" + "="*25)
        print(f"💵 Current balance: ${self.resources['money']:.2f}")
        try:
            amount = float(input("Enter amount to collect: $"))
            if 0 < amount <= self.resources['money']:
                self.resources['money'] -= amount
                print(f"✅ Collected ${amount:.2f}")
                print(f"Remaining balance: ${self.resources['money']:.2f}")
                self.log_operation("MONEY", f"Collected ${amount:.2f}")
            else:
                print("❌ Invalid amount!")
        except ValueError:
            print("⚠️ Please enter a valid number!")

    def show_history(self) -> None:
        """Показывает историю операций"""
        print("\n" + "="*25)
        print("=== OPERATION HISTORY ===")
        print("="*25)
        for record in self.operation_history[-10:]:
            print(record)
        input("\nPress Enter to return to menu...")

    def run(self) -> None:
        """Основной цикл работы кофемашины"""
        print("\n" + "="*25)
        print("=== COFFEE MACHINE OOP ===")
        print("="*25)
        self.log_operation("SYSTEM", "Machine started")
        
        while True:
            self.check_auto_refill()
            
            choice = input("\nMain menu:\n"
                          "1. Order (espresso/latte/cappuccino)\n"
                          "2. Report\n"
                          "3. Service Mode\n"
                          "4. Collect Money\n"
                          "5. Show History\n"
                          "6. Turn Off\n"
                          "Your choice: ").lower()
            
            if choice == '6' or choice == 'off':
                self.log_operation("SYSTEM", "Machine stopped")
                print("\nTurning off the machine... Goodbye!")
                break
                
            elif choice == '2' or choice == 'report':
                self.show_resources()
                
            elif choice == '3' or choice == 'service':
                self.service_mode()
                
            elif choice == '4' or choice == 'collect':
                self.collect_money()
                
            elif choice == '5' or choice == 'history':
                self.show_history()
                
            elif choice in self.MENU:
                self.process_order(choice)
            else:
                print("\n⚠️ Invalid choice. Please try again.")

    def process_order(self, drink: str) -> None:
        """Обрабатывает заказ напитка"""
        missing = self.check_resources(drink)
        if missing:
            print(f"\n⚠️ Sorry, not enough {', '.join(missing)}.")
            self.log_operation("ERROR", f"Not enough {', '.join(missing)} for {drink}")
            return
            
        print(f"\nPrice: ${self.MENU[drink]['cost']:.2f}")
        payment = self.process_coins()
        
        if payment < self.MENU[drink]['cost']:
            print("\n❌ Sorry, that's not enough money. Money refunded.")
            self.log_operation("ORDER", f"{drink} - Payment failed")
        else:
            change = round(payment - self.MENU[drink]['cost'], 2)
            if change > 0:
                print(f"\nHere's ${change:.2f} in change.")
            self.resources['money'] += self.MENU[drink]['cost']
            self.make_drink(drink)
            self.log_operation("ORDER", f"Success: {drink} ${self.MENU[drink]['cost']:.2f}")

# Запуск кофемашины
if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.run()