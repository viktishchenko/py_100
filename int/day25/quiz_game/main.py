import turtle
import get_coordinates
import pandas

screen = turtle.Screen()
screen.title('States Game (US)')
image = 'day25/quiz_game/blank_states_img.gif'
screen.addshape(image)


turtle.shape(image)

city = turtle.Turtle()
city.hideturtle()
city.pu()



# print(f'user_answer>>> {user_answer}')

pd = pandas
data = pd.read_csv('day25/quiz_game/50_states.csv')
# print(data['state'])
game_is_on = True

while game_is_on:
  user_answer = screen.textinput(title='Gess the State', prompt="What\'s another state\'s name?")

  for state in data['state']:
    if user_answer == state:
      print(state)
      coor = data[data['state']==state]
      city.goto(coor.x.iloc[0], coor.y.iloc[0])
      city.write(state, font=('Arial',16, 'normal'))

  if user_answer not in data['state'].to_list():
    game_is_on = False
    city.goto(0,0)
    city.color('red')
    city.write('Sorry, you lose!', font=('Arial',12, 'normal'))
    print('Bye!')

  


  # if state != user_answer:
  #   print('Bye')
  #   game_is_on = False



# turtle.onscreenclick(get_coordinates.mouse_click_coor)
# KEEP SCREEN OPEN
turtle.mainloop()
# CLOSE SCREEN ON CLICK
# screen.exitonclick()