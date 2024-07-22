import time
from random import randint
import turtle

screen = turtle.Screen()
screen.bgcolor("light blue")
game_over = False
score = 0
FONT1 = ('Arial', 25, 'bold')
FONT2 = ('Arial', 30, 'bold')
FONT3 = ('Arial', 40, 'bold')

count_down_turtle = turtle.Turtle()
score_turtle = turtle.Turtle()

mike = turtle.Turtle()
mike.hideturtle()
mike.penup()
mike.shape('turtle')
mike.shapesize(2, 2)
mike.color("dark green")
def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()
    score_turtle.setposition(0, 300)
    score_turtle.write(arg='Score: 0', move=False, align='center', font=FONT1)

def change_position():
    mike.hideturtle()
    mike.goto(randint(-300, 0), randint(0, 300))
    mike.showturtle()

def turtle_click(x, y):
    global score
    score += + 1
    score_turtle.clear()
    score_turtle.write(F"Score: {score}", move=False, align="center", font=FONT1)
    change_position()

def countdown(time):
    global game_over
    global score
    count_down_turtle.hideturtle()
    count_down_turtle.penup()
    count_down_turtle.setposition(0, 350)
    count_down_turtle.clear()

    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write(f"Time: {time}",move=False,align="center",font=FONT2)
        change_position()
        screen.ontimer(lambda: countdown(time - 1), 1000)
    elif score >= 5:
        game_over = True
        count_down_turtle.clear()
        mike.hideturtle()
        count_down_turtle.setposition(0, 0)
        count_down_turtle.color("red")
        count_down_turtle.write("WIN!", align='center', font=FONT3)
    else:
        game_over = True
        count_down_turtle.clear()
        score_turtle.clear()
        mike.hideturtle()
        count_down_turtle.setposition(0, 0)
        count_down_turtle.color("red")
        count_down_turtle.write("GAME OVER!", align='center', font=FONT3)

def start_game_up():
    global game_over
    game_over = False
    turtle.tracer(0)
    setup_score_turtle()
    mike.onclick(turtle_click)
    turtle.tracer(1)
    screen.ontimer(lambda: countdown(10), 10)

start_game_up()
turtle.mainloop()