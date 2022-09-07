import colorgram
import turtle as t
import random
from color_list import sunset_colours

# rgb_colors = []
# colors = colorgram.extract('sunset.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)


print(sunset_colours)
nika = t.Turtle()
screen = t.Screen()
nika.speed(0)
nika.penup()
nika.hideturtle()

nika.setheading(225)
nika.forward(300)
nika.setheading(0)

screen.
print(screen.screensize())
screen.colormode(255)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    nika.dot(20, random.choice(sunset_colours))
    nika.forward(50)

    if dot_count % 10 == 0:
        nika.setheading(90)
        nika.forward(50)
        nika.setheading(180)
        nika.forward(500)
        nika.setheading(0)


screen.exitonclick()