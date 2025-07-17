from random import randint


HARD = 5
EASY = 10
DIFFICULTY = 0
game_over = False

print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')

choise = input('Choose a difficulty. Type \'easy\' or \'hard\': ')

if choise == 'easy':
  DIFFICULTY = EASY
else:
  DIFFICULTY = HARD

guessing_num = randint(1,100)
# guessing_num = random.choice(range(1,101))
print(f'guessing_num: {guessing_num}')
print(f'difficulty: {DIFFICULTY}')
print(f'You have {DIFFICULTY} attempts remaining to guess the number.')

while not game_over:
  DIFFICULTY  -= 1
  guess = int(input('Make a gues: '))
  print(f'guess: {guess}')
  if guess < guessing_num:
    print('Too low')

  if guess > guessing_num:
    print('Too high')

  if guess == guessing_num:
    print(f'You cuess! Guessing number is: {guessing_num}')
    game_over = True
    break

  if DIFFICULTY == 0:
    print(f'You lose. Guessing number is: {guessing_num}')
    game_over = True
    break

  print(f'You have {DIFFICULTY} attempts remaining to guess the number.')
  print('Guess again.')




