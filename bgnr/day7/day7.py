import random
import hangman_module

word_list = 'camel', 'baboon', 'aardvark'
chosen_word = random.choice(word_list)

print(' '.join(chosen_word))
game_over = False

placeholder = ''
for el in range(len(chosen_word)):
  placeholder += '_' 
print(' '.join(placeholder))

correct_letters = []
lives = len(hangman_module.HANGMANPICS) - 1
print(hangman_module.HANGMANPICS[lives])

while not game_over:
  print(f'lives>>> {lives}')
  guess = input('Gess a letter: ').lower()  

  if len(guess) !=1 or not guess.isalpha() :
    print('You can check only one character!')
    continue

  if guess in correct_letters:
    print('You are already guess this letter.')
    continue

  if not guess in chosen_word:
    print(f'There\'s no letter "{guess}" in this word.')
    lives -= 1
    print(hangman_module.HANGMANPICS[lives])
    if lives == 0:
      game_over = True
      print('You lose!')

  display = ''

  for letter in chosen_word:
    if letter == guess:
      display += letter
      print(f'Yep you guess it!')
      print(hangman_module.HANGMANPICS[lives])
      if lives == 0:
        game_over = True
        print('You lose!')
      correct_letters.append(guess)
    elif letter in correct_letters:
      display += letter
    else:
      display += '_'

  print(' '.join(display))

  if '_' not in display:
    game_over = True
    print('You win!')
