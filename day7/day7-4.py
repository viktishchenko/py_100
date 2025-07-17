import random

guess_list = ['apple', 'banana','cherry']
guess_word = random.choice(guess_list)

print('Добро пожаловать на игру висельник!')
print(' '.join(guess_word))
display = ['_' for _ in guess_word]
print(' '.join(display))

guess_letter_list = []
game_over = False

while not game_over:
  guess_letter = input('Введите вашу букву: ').lower()

  if len(guess_letter) !=1 or not guess_letter.isalpha():
    print('Ввести можно только одну букву!')
    continue

  if guess_letter in guess_letter_list:
    print(f'Вы уже выбирали букву {guess_letter}')
    continue


  if guess_letter in guess_word:
    guess_letter_list.append(guess_letter)
    print(f'Вы угадали буква {guess_letter}, есть в загаданном слове!')
    
    for i, letter in enumerate(guess_word):
      if letter == guess_letter:
        display[i] = letter

  else:
    print(f'Буквы {guess_letter}, нет в загаданном слове!')

  print(' '.join(display))

  if '_' not in display:
    game_over = True
    print('Вы выйграли, поздравляем!')
