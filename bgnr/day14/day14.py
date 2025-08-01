import py_art
import game_data
import random

SCORE = 0
DATA_A = {}
DATA_B = {}
GAME_OVER = False

def get_random_data(g_data, quantity=2):
  datas = [random.choice(g_data) for _ in range(quantity)]
  global DATA_A
  DATA_A = datas[0]
  global DATA_B
  DATA_B = datas[1]
  # DATA_A = random.choice(datas)
  # DATA_B = random.choice(datas)
  # if DATA_A == DATA_B:
  #   DATA_B = random.choice(datas)
  # print(f'compare>>> {DATA_A['follower_count']}/{DATA_B['follower_count']}')


def compare_data(user_a):

  # if a_followers > b_followers:
  #     return guess == "a"
  # else:
  #     return guess == "b"

  if int(DATA_A['follower_count']) > int(DATA_B['follower_count']) and user_a == 'a':
    return 'a'
  elif int( DATA_A['follower_count']) < int(DATA_B['follower_count']) and user_a == 'b':
    return 'b'



while not GAME_OVER:
  print(py_art.logo)
  if SCORE > 0:
    print(f'Your score is: {SCORE}, let\'s rock!')

  get_random_data(game_data.data)

  print(f'Compare A: {DATA_A['name']}, a {DATA_A['description']}, from {DATA_A['country']}')
  print(py_art.vs)
  print(f'Compare B: {DATA_B['name']}, a {DATA_B['description']}, from {DATA_B['country']}')
  user_answer = input('Who has more followers? Type "A" or "B": ').lower()
  print(compare_data(user_answer))
  if user_answer == compare_data(user_answer):
    SCORE += 1
    print(f'You\'re right! Current score: {SCORE}.')
  else:
    print(py_art.logo)
    print(f'Sorry, it\'s wrong, your score is: {SCORE}.')
    GAME_OVER = True