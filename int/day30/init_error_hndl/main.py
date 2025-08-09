# FileNotFoundError___________________
# with open('int/day30/init_error_hndl/data.txt') as file:
#   file.read() # FileNotFoundError: [Errno 2] No such file or directory: 'int/day30/init_error_hndl/data.txt'

try:
  file = open('int/day30/init_error_hndl/data.txt') # Error
  # a_dictionary = {'key': 'value'}
  # a_dictionary['abra_kadabra'] # Error
except FileNotFoundError:
  file = open('int/day30/init_error_hndl/data.txt', 'w') # create file data.txt
  file.write('Halo, there!') # write:Halo there!
except KeyError as error_message:
  print(f'That key:{error_message} does not exist.') # That key:'abra_kadabra' does not exist.
# except KeyError:
#   print('That key does not exist') # That key does not exist
else: # ONLY IF TRY CORRECT!!!
  content = file.read()
  print(f'content>>> {content}') # content>>> Halo, there!
finally:
  file.close()
  print('File was closed.') # File was closed.


# KeyError____________________________
# a_dictionary = {'key': 'value'}
# value = a_dictionary['not_existen_key'] # KeyError: 'not_existen_key'

# IndexError__________________________
# fruit_list = ['Apple','Banana','Pear']
# fruit_list[3] # IndexError: list index out of range

# TypeError
# text = 'abc'
# print(text + 5) # TypeError: can only concatenate str (not "int") to str

# CATCHING EXEPTIONы (ERROR HANDLING)
try:
  pass
# smth might cause exeption
except:
  pass
# do this if there was exeption
else:
  pass
# do this if there were no exeption
finally:
  pass
# do this no matter what happens
