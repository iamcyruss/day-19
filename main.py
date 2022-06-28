from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_right():
    new_right_heading = tim.heading() - 10
    tim.setheading(new_right_heading)


def move_left():
    new_left_heading = tim.heading() + 10
    tim.setheading(new_left_heading)


def clear_screen():
    screen.reset()


def change_color():
    tim.color(random.choice(range(256)), random.choice(range(256)), random.choice(range(256)))


screen.listen()
tim.speed("fastest")
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="z", fun=change_color)


screen.exitonclick()
