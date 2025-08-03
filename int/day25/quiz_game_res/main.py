import turtle
import get_coordinates
import pandas

screen = turtle.Screen()
screen.title('States Game (US)')
image = 'int/day25/quiz_game_res/blank_states_img.gif'
screen.addshape(image)


turtle.shape(image)

city = turtle.Turtle()
city.hideturtle()
city.pu()

pd = pandas
data = pd.read_csv('int/day25/quiz_game_res/50_states.csv')
all_states = data.state.to_list()
print(f'all_states>>> {all_states}')
guessed_states = []
learn_states = all_states

game_is_on = True

while game_is_on:

  user_answer = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt='What\'s another state\'s name?').title()

  if user_answer=='Exit':
    # OR
    # missing_states = []
    # for state in all_states:
    #   if state not in guessed_states:
    #     missing_states.append(state)
    # new_data = pd.DataFrame(missing_states)
    # new_data.to_csv('int/day25/quiz_game_res/learn_sates.csv')

    get_learn()
    break
    
  def get_learn():
    pd.DataFrame(learn_states).to_csv('int/day25/quiz_game_res/learn_sates.csv')
    
    


  print(f'user_answer>>> {user_answer}')

  if user_answer in all_states:
    guessed_states.append(user_answer)
    city_data = data[data.state==user_answer]
    city.goto(city_data.x.item(),city_data.y.item())
    city.write(user_answer, align='center', font=('Arial', 12, 'normal'))

  # STATE TO LEARN
  for state in all_states:
    if state in guessed_states:
      learn_states.remove(state)
    


  if user_answer not in data['state'].to_list():
    print('Bye!')
    game_is_on = False
    city.goto(0,0)
    city.color('red')
    city.write('Wrong answer!', align='center', font=('Arial', 18, 'bold'))
    get_learn()
    





# turtle.onscreenclick(get_coordinates.mouse_click_coor)
# KEEP SCREEN OPEN
# turtle.mainloop()
# CLOSE SCREEN ON CLICK
# screen.exitonclick()