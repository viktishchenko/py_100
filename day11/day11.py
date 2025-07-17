import art
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def get_card(quantity=1):
  return [random.choice(cards) for _ in range(quantity)]

def get_card_sum(arr):
    total = sum(arr)
    if total > 21 and 11 in arr:  # Если перебор и есть туз
        arr[arr.index(11)] = 1     # Заменяем 11 на 1
        return get_card_sum(arr)   # Пересчитываем сумму
    return total

def get_one_more_card(prev):
  for card in get_card():
    prev.append(card)
  return prev


def init_game():
  print(art.logo)
  welcome = input('Do you want to play a game of Blackjack? Type "y" or "n": ')

  if welcome == 'y':
    user_init_cards = get_card(2)
    user_init_cards_sum = get_card_sum(user_init_cards)
    if user_init_cards_sum == 21:
      print('You win!')
      init_game()
      
    if user_init_cards_sum > 21:
      print(f'Your cards: {user_init_cards}, current score: {user_init_cards_sum}')
      print('You lose 😤')
      init_game()
    computer_init_cards = get_card()
    computer_init_cards_sum = get_card_sum(computer_init_cards)

    print(f'Your cards: {user_init_cards}, current score: {user_init_cards_sum}')
    print(f'Computer\'s first card: { computer_init_cards_sum}')

    should_continue = True

    if should_continue == True:
      while should_continue == True:
        get_one_more = input('Type "y" to get another card, type "n" to pass:\n')
        if get_one_more == 'y':
          user_current_cards = get_one_more_card(user_init_cards)
          user_current_sum = get_card_sum(user_current_cards)

          print(f'Your cards: {user_current_cards}, current score: {user_current_sum}')

          if user_current_sum == 21:
            print('You win!')
            should_continue = False
            init_game()

          if user_current_sum > 21:
            print('Bust, you lose 😤')
            should_continue = False
            init_game()
        else:
          computer_current_sum = computer_init_cards_sum
          while computer_current_sum < 17:
            computer_current_cards = get_one_more_card(computer_init_cards)
            computer_current_sum = get_card_sum(computer_current_cards)
          
          print(f'Computer\'s final hand: {computer_current_cards}, final score: {computer_current_sum}')
          user_sum = get_card_sum(user_init_cards)
          # print(f'user sum: {user_sum}')

          if computer_current_sum > 21:
            print('Opponent went over. You win 😁')
            should_continue = False
            init_game()
          elif user_sum == computer_current_sum:
            print('Push, hands of equal value')
            should_continue = False
            init_game()
          elif user_sum > computer_current_sum:
            print('You win 😁')
            should_continue = False
            init_game()
          else:
            print('You lose 😤')
            should_continue = False
            init_game()

  else:
    print('Have a nice day!')
    exit()

init_game()