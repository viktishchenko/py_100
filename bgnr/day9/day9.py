import art_module

print('Halo another one app')
print(art_module.art)

should_continue = True
user_dictionary = {}

def check_users_bid(info):
      print(info)
      # max_val = 0
      # winner = ''
      # for user in info:
      #   res = int(info[user])
      #   if max_val < res:
      #      max_val = res
      #      winner = user
       
      # print(f'The winner is {winner} with result {max_val}$.')

      winner_name = max(info, key = info.get)
      win_bid = 0
      for user in info:
         if user == winner_name:
            win_bid = info[user]
            
      print(f'The winner is {winner_name} with result {win_bid}$.')


      # max_value = max(zip(info.values(), info.keys()))
      # print(f'The winner is {max_value[1]} with result {max_value[0]}$.')

while should_continue:

  user_name = input('What is your name: ')
  user_value = input('What is your bit: $')

  user_dictionary[user_name] = user_value

  add_another = input('Another one? Type y to "yes" or n to "n" ').lower()
  if add_another == 'y':
    should_continue = True
  else:
    check_users_bid(user_dictionary)
    should_continue = False

