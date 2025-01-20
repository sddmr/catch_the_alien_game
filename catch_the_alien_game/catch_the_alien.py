import turtle
import random

# Create screen
alien_screen = turtle.Screen()
alien_screen.bgcolor("gray10")
alien_screen.title("Catch the Alien")

# Add hero image
hero_path = "hero.gif"
alien_screen.addshape(hero_path)

# Add hero character
hero = turtle.Turtle()
hero.shape(hero_path)
hero.penup()
hero.hideturtle()

# Create the score counter
score = turtle.Turtle()
score.hideturtle()
score.penup()
score.goto(0, 200)  # Position of the score counter
score.color("green")

# Create the timer
timers = turtle.Turtle()
timers.hideturtle()
timers.penup()
timers.goto(0, 250)
timers.color("white")

# Global variables
current_score = 0
time_left = 30
game_active = True

# Function to update the score
def update_score():
    score.clear()
    score.write(f"Score: {current_score}", align="center", font=("Arial", 20, "bold"))

# Countdown function
def countdown(saniye):
    global game_active
    if saniye > 0:
        timers.clear()
        timers.write(f"Time Left: {saniye} seconds", align="center", font=("Arial", 20, "bold"))
        alien_screen.ontimer(lambda: countdown(saniye - 1), 1000)
    else:
        timers.color("red")
        game_active = False  # Disable the game
        hero.hideturtle()  # Hide the character
        timers.clear()
        timers.write("Time's Up!", align="center", font=("Arial", 20, "bold"))

# Function to move the character to a random position
def move_hero():
    if game_active:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        hero.goto(x, y)
        hero.showturtle()
        alien_screen.ontimer(move_hero, 100)  # Call again after 0.01 second

# Increase score when the character is clicked
def on_hero_click(x, y):
    global current_score
    if game_active:
        current_score += 1
        update_score()
        hero.hideturtle()  # Hide the character

# Bind the click event
hero.onclick(on_hero_click)

# Start the score
update_score()

# Start the countdown
countdown(time_left)

# Start moving the character
move_hero()

# Keep the program open
turtle.mainloop()
