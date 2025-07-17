import turtle
import get_coordinates
import pandas

screen = turtle.Screen()
screen.title('States Game (US)')
image = 'day25/quiz_game_res/blank_states_img.gif'
screen.addshape(image)


turtle.shape(image)

city = turtle.Turtle()
city.hideturtle()
city.pu()

pd = pandas
data = pd.read_csv('day25/quiz_game_res/50_states.csv')
# print(data)
# print(data['state'][0]) # Alabama
# print(data['x'][0]) # 139
# print(data['y'][0]) # -77

game_is_on = True

while game_is_on:

  user_answer = screen.textinput('Gess the state', prompt='What\'s another state\'s name?')

  if user_answer in data['state'].to_list():
    city_data = data[data.state==user_answer]
    # city_data = data[data['state']==user_answer]
    city.goto(city_data.x.iloc[0],city_data.y.iloc[0])
    city.write(user_answer, align='center', font=('Arial', 12, 'normal'))

  if user_answer not in data['state'].to_list():
    print('Bye!')
    game_is_on = False
    city.goto(0,0)
    city.color('red')
    city.write('Wrong answer!', align='center', font=('Arial', 18, 'bold'))
    





# turtle.onscreenclick(get_coordinates.mouse_click_coor)
# KEEP SCREEN OPEN
turtle.mainloop()
# CLOSE SCREEN ON CLICK
# screen.exitonclick()