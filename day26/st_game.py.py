import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("US States Game")
image = "day25/quiz_game_res/blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)


data = pd.read_csv("day25/quiz_game_res/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="Enter the name of the state:").title()

    if answer_state == "Exit":
        
        # missing_states = [new_item  for item in all_states if test]

        # missing_states = []
        # for state in all_states:
        #   if state not in guessed_states:
        #     missing_states.append(state)
        
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break


    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)