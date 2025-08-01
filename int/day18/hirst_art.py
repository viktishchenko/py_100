import turtle as t
import random

# py -m pip install colorgram // add colorgram
# import colorgram
# rgb_colors = []
# colors = cologram.extract('img_name.jpg', 30)
# for color of colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_colors = (r, g, b)
#   rgb_colors.append(new_colors)
# color_list = print(rgb_colors)

color_list = [(186, 168, 18), (61, 251, 188), (9, 65, 77), (62, 63, 55), (175, 207, 5), (60, 174, 194), (217, 191, 176), (211, 225, 228), (27, 0, 39), (178, 65, 19), (109, 
154, 185), (217, 66, 188), (180, 5, 119), (95, 210, 209), (211, 240, 112), (58, 129, 119), (59, 75, 222), (169, 182, 93)]

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()

tim.hideturtle()
tim.pu()
tim.speed(0)
tim.seth(220)
tim.forward(300)
tim.seth(0)

num_of_dots = 100

for dot_count in range(1,num_of_dots + 1):
  tim.dot(20, random.choice(color_list))
  tim.forward(50)

  if dot_count % 10 == 0:
    tim.seth(90)
    tim.forward(50)
    tim.seth(180)
    tim.forward(500)
    tim.seth(0)


# for _ in range(10):

#   for _ in  range(10):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)

#   tim.seth(90)
#   tim.forward(50)
#   tim.seth(180)
#   tim.forward(500)
#   tim.seth(0)

screen.exitonclick()