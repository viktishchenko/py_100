import random

word_list = 'camel', 'baboon', 'aardvark'
chosen_word = random.choice(word_list)

print(chosen_word)
game_over = False

placeholder = ''
for el in range(len(chosen_word)):
  placeholder += '_' 
print(' '.join(placeholder))

correct_letter = []

while not game_over:
  guess = input('Gess a letter: ').lower()  

  display = ''

  for letter in chosen_word:
    if letter == guess:
      display += letter
      correct_letter.append(guess)
    elif letter in correct_letter:
      display += letter
    else:
      display += '_'

  print(' '.join(display))

  if '_' not in display:
    game_over = True
    print('You win!')