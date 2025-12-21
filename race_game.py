import turtle
import random
import time

def turtle_race():
    screen = turtle.Screen()
    screen.bgcolor("lightgreen")
    screen.title("Five Turtles Race Game") 

    #Create race track
    track = turtle.Turtle()
    track.speed(0)
    track.penup()

    track.goto(-300, 150)
    track.pendown()
    track.color("red")
    track.width(3)
    track.goto(-300, -150)

    track.penup()
    track.goto(300, 150)
    track.pendown()
    track.color("blue")
    track.width(3)
    track.goto(300, -150)

    #Create turtles
    colors = ["red", "pink", "white", "black", "grey"]
    turtles = []

    for i, color in enumerate(colors):
        t = turtle.Turtle()
        t.shape("turtle")
        t.color(color)
        t.penup()
        t.goto(-320, 100 - i * 40)
        turtles.append(t)

    #count down
    countdown = turtle.Turtle()
    countdown.penup()
    countdown.hideturtle()
    countdown.goto(0, 200)

    for i in range(3, 0, -1):
        countdown.write(str(i), align="center", font=("Arial", 48, "normal"))
        time.sleep(1)
        countdown.clear()

    countdown.write("Go!", align="center", font=("Arial", 48, "normal"))
    time.sleep(0.5)
    countdown.clear()

    #Race
    winner = None
    while not winner:
        for t in turtles:
            #Move turtles forward by random distance
            distance = random.randint(1, 10)
            t.forward(distance)

            #Check for winner
            if t.xcor() >= 300:
                winner = t
                break


    #Announce winner
    countdown.goto(0,0)
    countdown.color(winner.color()[0])
    countdown.write(f"The winner is the {winner.color()[0]} turtle!", align="center", font=("Arial", 24, "bold"))






    screen.mainloop()

turtle_race()