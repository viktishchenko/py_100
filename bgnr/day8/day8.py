import re
import logo

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


print(logo.logo)
print('Welcome to Caesar Cipher!')

def encode(original_text, shift_amount):
  cipher_text = ''
  for letter in original_text:
    if direction == 'encode':
      # shift_amount *= -1 # меняем знак на противоположный
      shifted_position = alphabet.index(letter) + shift_amount
    elif direction == 'decode':
      shifted_position = alphabet.index(letter) - shift_amount
    else:
      print('Something gone wrong!')
      exit()

    shifted_position %= len(alphabet)
    cipher_text += alphabet[shifted_position]

  print(f'Here is {direction}d result: {cipher_text}')


should_continue = True

while should_continue:
  print('________________________')
  direction = input('Type "encode" to encript, type "decode" to decript:\n').lower()

  if direction !='encode' and direction !='decode':
    print('Type more carefully!')
    exit()
  
  text = input('Type yor message:\n').lower()

  if re.search(r'\d', text):
    print('you can\'t add digits')
    exit()

  if re.search(r' ', text):
    print('you can\'t add spaces!')
    exit()


  shift = int(input('Type the shift number:\n'))
  encode(original_text=text, shift_amount=shift)

  should_continue = input('Do you want to continue? Type y to "yes" and n to "no"\n')

  if should_continue == "n":
    should_continue = False
    print('Bye!')


# def encode(original_text, shift_amount):
#   cipher_text = ''
#   for letter in original_text:
#     shifted_position = alphabet.index(letter) + shift_amount

#     shifted_position %= len(alphabet)
#     cipher_text += alphabet[shifted_position]

#   print(f'Here is encoded result: {cipher_text}')

# def decript(text,shift):
#   decript_text = 
#   print('Halo decript!')

# if direction == 'encode':
#   encode(original_text=text, shift_amount=shift)
# elif direction == 'decode':
#   decript()
# else:
#   print('You type something wrong...')