greet = 'Halo'

def print_foo(arg):
  print(arg)

def greet_function():
  res = greet + ' there' + '!'
  print_foo(res)

greet_function() # Halo there!

for step in range(4): # 5 Time - Halo there!
  greet_function()


# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     while not right_is_clear():
#         move()
#     else:
#         turn_right()
#         move()
#         turn_right()
#         while not wall_in_front():
#             move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# Maze



# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def walk():
#     while not wall_in_front():
#         move()
#         if not wall_on_right():
#             if at_goal():
#                 done()
#             else:
#                 turn_right()
                
# while not at_goal():
#     walk()
#     if not wall_on_right():
#         turn_right()
#         walk()
#     elif wall_on_right() or wall_in_front():
#         turn_left()
#         walk()

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while front_is_clear():
#     move()
# turn_left()
                
# while not at_goal():
#     if(right_is_clear()):
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()