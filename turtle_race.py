import turtle
import random

def turtle_race():

    turt1 = turtle.Turtle()
    turt2 = turtle.Turtle()
    turt3 = turtle.Turtle()
    turt4 = turtle.Turtle()
    turt5 = turtle.Turtle()
    turt6 = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(height=400, width=670)

    turtles = [turt1, turt2, turt3, turt4, turt5, turt6]
    colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange']
    i = 0
    y = -100


    for turt in turtles:
        turt.penup()
        turt.color(colors[i])
        i += 1
        turt.shape('turtle')
        turt.goto(-250, y)
        y += 50

    user_bet = screen.textinput(title='Place Your Bet!',
                                prompt="Which colour will win? ")

    k = True

    while k:
        for turt in turtles:
            x, y = turt.pos()
            turt.goto(random.randint(0, 10)+x, y)
            if turt.xcor() > 300:
                k = False

                if user_bet == turt.color()[0]:

                    result = "Yay!! you won."
                else:
                    result = 'you lose.'
                print(f'{result} Winner is {turt.color()[0]}')
                break  # for loop runs for all elements in turtles so if green won but loop not exit another can win like orange '22-6-2023,20:38' so beak end loop as soon as anyone won


    screen.exitonclick()
turtle_race()