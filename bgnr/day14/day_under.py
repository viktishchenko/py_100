import py_art
import os
import game_data
import random

SCORE = 0
DATA_A = {}
DATA_B = {}
GAME_OVER = False

def clear_screen():
    """Очищает консоль для разных ОС"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_data(g_data, quantity=2):
  datas = [random.choice(g_data) for _ in range(quantity)]
  global DATA_A
  DATA_A = datas[0]
  global DATA_B
  DATA_B = datas[1]
  print(f'compare>>> {DATA_A['follower_count']}/{DATA_B['follower_count']}')


def compare_data(user_choice):
  follower_a = int(DATA_A['follower_count'])
  follower_b = int(DATA_B['follower_count'])

  if follower_a == follower_b:
    return None
  
  return (follower_a > follower_b and user_choice == 'a') or (follower_b > follower_a and user_choice == 'b')
  # if int(DATA_A['follower_count']) > int(DATA_B['follower_count']) and user_choice == 'a':
  #   return 'a'
  # elif int( DATA_A['follower_count']) < int(DATA_B['follower_count']) and user_choice == 'b':
  #   return 'b'



while not GAME_OVER:
  clear_screen()
  print(py_art.logo)
  if SCORE > 0:
    print(f'Your score is: {SCORE}, let\'s rock!')

  get_random_data(game_data.data)

  print(f'Compare A: {DATA_A['name']}, a {DATA_A['description']}, from {DATA_A['country']}')
  print(py_art.vs)
  print(f'Compare B: {DATA_B['name']}, a {DATA_B['description']}, from {DATA_B['country']}')

  while True:
    user_choice = input('Who has more followers? Type "A" or "B": ').lower()
    if user_choice in ('a', 'b'):
      break
    print('Invalid input! Try again.')


  is_correct = compare_data(user_choice)
  if is_correct is None:
    print('its draw ====')
  elif is_correct:
    SCORE += 1
    print(f'norm, your score: {SCORE}')
  else:
    print(f'Wrong answer, your score {SCORE}')
    GAME_OVER = True

  if not GAME_OVER:
    input('Press Enter to continue...')