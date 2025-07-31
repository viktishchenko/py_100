# COLORHUNT

from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='day28/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(105,140, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1,row=1)

timer_title = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 46, 'bold'))
timer_title.grid(column=1,row=0)

def start_timer():
  print('start')

def reset_timer():
  print('reset')

start_button = Button(text='Start',padx=10,pady=5, font=('Arial', 16, 'normal'), highlightcolor="#bdbdbd", command=start_timer, highlightbackground="#bdbdbd",borderwidth=1)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset',font=('Arial', 16, 'normal'),highlightcolor="#bdbdbd", command=reset_timer, highlightbackground="#bdbdbd",borderwidth=1)
reset_button.grid(column=2,row=2)

timer_check = Label(text='✔', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, 'bold'))
timer_check.grid(column=1,row=3)





window.mainloop()