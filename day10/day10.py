# DOC.STRING.EX.
def change_name (first,last):
  ''' Take a first and last name and format
  it to return the title case of the name.'''
  first_name = first.title()
  # first_name = first.lower().capitalize()
  last_name = last.title()
  # last_name = last.lower().capitalize()
  return f'{last_name} {first_name}'

result_format = change_name('VIK', 'tI')
print(result_format)