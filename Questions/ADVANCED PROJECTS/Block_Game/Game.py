
## A game Using Turtle in python this is a Dodging game 
# If player Hit by Objects The game Over

import turtle
import random

# --- Screen Setup ---
screen = turtle.Screen()
screen.title("Turtle Dodger Game")
screen.bgcolor("red")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic screen updates

# --- Player Setup ---
player = turtle.Turtle()
player.shape("turtle")
player.color("black")
player.penup()
player.goto(0, -250)
player.setheading(90)
player.speed(0)

# --- Player Movement Functions ---
def go_left():
    x = player.xcor()
    if x > -380:
        player.setx(x - 20)

def go_right():
    x = player.xcor()
    if x < 380:
        player.setx(x + 20)

# --- Block Setup ---
block = turtle.Turtle()
block.shape("square")
block.color("purple")
block.penup()
block.shapesize(stretch_wid=1, stretch_len=3)
block.speed(0)
block.goto(random.randint(-380, 380), 300)

# --- Score Display ---
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)
score = 0
score_display.write(f"Score: {score}", align="center", font=("Arial", 18, "normal"))

# --- Game Variables ---
speed = 0.2
game_on = True

# --- Keyboard Bindings ---
screen.listen()
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

def exit_game():
    global game_on
    game_on = False
    screen.bye()

screen.onkeypress(exit_game, "Escape")

# --- Game Loop ---
while game_on:
    screen.update()

    # Move the block
    y = block.ycor()
    block.sety(y - speed)

    # Check if block hits the player
    if block.distance(player) < 20:
        game_on = False
        score_display.clear()
        score_display.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    # Check if block reached the bottom
    if block.ycor() < -280:
        block.goto(random.randint(-380, 380), 300)
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 18, "normal"))
        speed += 0.1  # Increase speed for difficulty

turtle.done()

