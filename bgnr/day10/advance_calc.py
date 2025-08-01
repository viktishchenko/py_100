import logo

print('Welcome to calculator app!')
print(logo.calc_logo)

def get_number(prompt):
    while True:
        num = input(prompt)
        try:
            return float(num)
        except ValueError:
            print("Please enter a valid number!")

def get_operation():
    while True:
        op = input('Pick an operation (+, -, *, /): ')
        if op in ('+', '-', '*', '/'):
            return op
        print("Invalid operation! Please choose +, -, *, or /")

def calculator():
    should_continue = True
    first_num = get_number('What\'s the first number?: ')
    
    while should_continue:
        print('+\n-\n*\n/')
        operation = get_operation()
        second_num = get_number('What\'s the next number?: ')

        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else "Error! Division by zero."
        }

        result = operations[operation](first_num, second_num)
        
        if isinstance(result, str):  # Если деление на ноль
            print(result)
            continue
        
        print(f'{first_num} {operation} {second_num} = {result}')

        choice = input(f'Type "y" to continue calculating with {result}, or "n" to start new: ').lower()
        if choice == 'y':
            first_num = result
        else:
            should_continue = False
            
calculator()  # Начинаем заново