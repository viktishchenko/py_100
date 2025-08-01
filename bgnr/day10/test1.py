import logo

print('Welcome to calulator!')
print(logo.calc_logo)

def get_number(promt):
  while True:
    num = input(promt)
    try:
      return num
    except ValueError:
      print('Pleace, enter a valid number!')
  

