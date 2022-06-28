from turtle import Turtle, Screen
import random


screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle do you think will win?\n"
                                                           "(red, orange, green, brown, blue, purple)\n"
                                                           "Enter color: ")
tim = Turtle()
tim.penup()
tim.color("red")
tim.shape("turtle")
tim.goto(x=-200, y=-150)
russ = Turtle()
russ.penup()
russ.color("orange")
russ.shape("turtle")
russ.goto(x=-200, y=-100)
jim = Turtle()
jim.penup()
jim.color("green")
jim.shape("turtle")
jim.goto(x=-200, y=-50)
john = Turtle()
john.penup()
john.color("brown")
john.shape("turtle")
john.goto(x=-200, y=0)
april = Turtle()
april.penup()
april.color("blue")
april.shape("turtle")
april.goto(x=-200, y=50)
joe = Turtle()
joe.penup()
joe.color("purple")
joe.shape("turtle")
joe.goto(x=-200, y=100)
turtle_names = [tim, russ, jim, john, april, joe]


def move_turtle(turtle_name):
    global keep_going
    global user_bet
    turtle_name.forward(random.choice(range(26)))
    if turtle_name.xcor() >= 200:
        print(f"And the winner is, {str(turtle_name.color()[0])}.")
        keep_going = False

        if user_bet == str(turtle_name.color()[0]):
            print(f"You guessed correct! \nYou're answer: {user_bet}\nAnd Winner was: {turtle_name.color()[0]}")
        else:
            print("You guessed wrong.")

        return keep_going


keep_going = True
while keep_going:
    move_turtle(random.choice(turtle_names))


screen.exitonclick()

