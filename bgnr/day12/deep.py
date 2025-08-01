from random import randint

HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10

print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')

# Выбор сложности с проверкой ввода
while True:
    choice = input('Choose a difficulty. Type "easy" or "hard": ').lower()
    if choice == 'easy':
        attempts = EASY_ATTEMPTS
        break
    elif choice == 'hard':
        attempts = HARD_ATTEMPTS
        break
    print('Invalid input! Please try again.')

guessing_num = randint(1, 100)
print(f'You have {attempts} attempts remaining to guess the number.')

# Основной цикл игры
while attempts > 0:
    try:
        guess = int(input('Make a guess: '))
    except ValueError:
        print('Please enter a number!')
        continue

    if guess < guessing_num:
        print('Too low.')
    elif guess > guessing_num:
        print('Too high.')
    else:
        print(f'You guessed it! The number was: {guessing_num}')
        break

    attempts -= 1
    if attempts > 0:
        print(f'You have {attempts} attempts remaining.')
        print('Guess again.')
    else:
        print(f'You lose. The number was: {guessing_num}')