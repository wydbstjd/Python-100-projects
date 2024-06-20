from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")
tim.color("red")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

# 정사각형 그리기
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
#
# 점선 그리기
# for i in range(0,10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# 다양한 도형 그리기
# num_side = 3
# for _ in range(6):
#     for _ in range(num_side):
#         angle = 360 / num_side
#         tim.forward(100)
#         tim.right(angle)
#     num_side += 1

#무작위 행보 구현하기
# directions = [0, 90, 180, 270]
# tim.width(15)
# tim.speed('fastest')
# for _ in range(100):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.right(random.choice(directions))

#Spirograph 구현하기
# tim.speed('fastest')

# def draw_spirodraph(size_of_gap):
#     for i in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirodraph(10)

#메인 프로젝트
#import colorgram

# rgb_colors = []
# colors = colorgram.extract('dot.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))

#print(rgb_colors)

color_list = [(241, 246, 242), (241, 242, 246), (199, 164, 111), (144, 76, 50), (62, 101, 129), (167, 150, 44), (218, 202, 138), (138, 164, 181), (130, 36, 22), (203, 93, 71), (53, 112, 81), (69, 47, 41), (144, 179, 150), (100, 82, 90), (232, 176, 163), (60, 48, 52), (20, 95, 70), (163, 146, 158), (39, 57, 75), (91, 150, 115), (96, 141, 151), (22, 86, 92), (76, 69, 46), (46, 63, 85), (114, 35, 39), (181, 203, 174), (86, 131, 173), (169, 100, 103)]
tim.speed('fastest')
tim.hideturtle()
for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        tim.penup()
        tim.setpos(x, y)

        tim.dot(30, random.choice(color_list))


screen = Screen()
screen.exitonclick()