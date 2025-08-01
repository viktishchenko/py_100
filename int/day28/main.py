# COLORHUNT
# WINDOW EMOJI WIN + ; OR WIN + .
# WIN + SHIFT + U → TO UPPERCASE
# WIN + SHIFT + L → TO LOWERCASE
# NAVIGATE BACK TO THE LAST CURSOR POSITION → (Alt + ←)

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .2
SHORT_BREAK_MIN = .1
LONG_BREAK_MIN = 20
reps = 0
timer = None
timer_on = False

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  window.after_cancel(timer)
  canvas.itemconfig(timer_text, text=f'00:00')
  timer_title.config(text='Timer', fg=GREEN)
  timer_check.config(text='')
  global reps, timer_on
  reps = 0
  timer_on = False


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global timer_on, reps

  if timer_on:
    return
  
  timer_on = True
  reps += 1

  work_sec = round(WORK_MIN * 60)
  short_break_sec = round(SHORT_BREAK_MIN * 60)
  long_break_min = round(LONG_BREAK_MIN * 60)

  if reps % 8 == 0:
    count_down(long_break_min)
    timer_title.config(text='Break', fg=RED)
  elif reps % 2 == 0:
    timer_title.config(text='Break', fg=PINK)
    count_down(short_break_sec)
  else:
    count_down(work_sec)
    timer_title.config(text='Work', fg=GREEN)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

  count_min = math.floor(count / 60)

  if count_min < 10:
    count_min = f'0{count_min}'

  count_sec = count % 60

  if count_sec < 10:
    count_sec = f'0{count_sec}'

  canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
  
  if count >= 0:
    global timer
    timer = window.after(1000, count_down, count-1)
  else:
    global timer_on
    timer_on = False
    start_timer()
    marks = ''
    work_session = math.floor(reps/2)
    for _ in range(work_session):
      marks += '✔'
    timer_check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='day28/img/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,140, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1,row=1)

timer_title = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 46, 'bold'))
timer_title.grid(column=1,row=0)

start_button = Button(text='Start',padx=10,pady=5, font=('Arial', 16, 'normal'), highlightcolor="#bdbdbd", command=start_timer, highlightbackground="#bdbdbd",borderwidth=1)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset',padx=10,pady=5,font=('Arial', 16, 'normal'),highlightcolor="#bdbdbd", command=reset_timer, highlightbackground="#bdbdbd",borderwidth=1)
reset_button.grid(column=2,row=2)

timer_check = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, 'bold'))
timer_check.grid(column=1,row=3)





window.mainloop()