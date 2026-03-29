# import colorgram
# rgb_colors= []
#
# # colors = colorgram.extract('image.jpg', 30)
# #
# # for color in colors:
# #     r = color.rgb.r
# #     g = color.rgb.b
# #     b = color.rgb.b
# #     new_color = (r,g,b)
# #     rgb_colors.append(new_color)
# #
# # print(rgb_colors)

import turtle
from turtle import Turtle
import random

turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
color_list = [(204, 107, 107), (239, 241, 241), (155, 46, 46), (235, 244, 244), (52, 123, 123), (224, 135, 135), (171, 40, 40), (138, 21, 21), (132, 185, 185), (200, 71, 71), (48, 87, 87), (14, 73, 73), (95, 75, 75), (146, 147, 147), (72, 38, 38), (163, 158, 158), (234, 165, 165), (55, 50, 50), (184, 172, 172), (19, 90, 90), (144, 24, 24), (41, 74, 74), (82, 128, 128), (181, 89, 89), (41, 90, 90), (13, 68, 68), (213, 183, 183), (179, 207, 207)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen  = turtle.Screen()
screen.exitonclick()