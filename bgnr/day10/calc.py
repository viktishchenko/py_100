import logo

print('Welcome to calculator app!')
print(logo.calc_logo)

should_continue = True

def calculator(f):

  first_num = f

  def add(n1,n2):
    return float(n1) + float(n2)

  def subtract(n1,n2):
    return float(n1) - float(n2)

  def multiply(n1,n2):
    return float(n1) * float(n2)

  def divide(n1,n2):
    return float(n1) / float(n2)

  operatins = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide,
}

  global should_continue
  if should_continue:
    first_num = input('What\'s the first number?:  ')

  for op in operatins:
    print(op)


  pic_operation = input('Pick an operation:  ')
  second_num = input('What\'s the next number:  ')

  result = operatins[pic_operation](first_num,second_num)

  print(f'{float(first_num)} {pic_operation} {float(second_num)} = {float(result)}')


  continue_calculating = input(f'Type "y" to continue calculating with {result}, or type "n" to start a new calculation:  ')

  if continue_calculating == 'y':
    should_continue = False
    first_num = result
    print('first_num>>>', first_num)
    calculator(first_num)
  else:
    exit()


calculator(f=0)