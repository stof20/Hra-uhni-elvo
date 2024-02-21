import turtle
import random
rychlost_objektu = 40

screen = turtle.Screen()
screen.title("Uhni želvo")
screen.bgpic("beachC.gif")
screen.setup(width=600, height=600)

hrac = turtle.Turtle()
hrac.shape("turtle")
hrac.right(90)
hrac.color("dark green")
hrac.penup()
hrac.speed(2)
hrac.goto(0, -250)

padajici_objekty = []

vystrely = []

skore = 0

text_skore = turtle.Turtle()
text_skore.speed(0)
text_skore.color("black")
text_skore.penup()
text_skore.hideturtle()
text_skore.goto(0, 260)
text_skore.write("Skóre: {}".format(skore), align="center", font=("Courier", 24, "normal"))

def pohyb_doleva():
    x = hrac.xcor()
    x -= 20
    if x < -280:
        x = -280
    hrac.setx(x)

def pohyb_doprava():
    x = hrac.xcor()
    x += 20
    if x > 280:
        x = 280
    hrac.setx(x)

def vystrel():
    vystrel = turtle.Turtle()
    vystrel.speed(0)
    vystrel.shape("triangle")
    vystrel.left(90)
    vystrel.color("brown")
    vystrel.shapesize(stretch_wid=0.5, stretch_len=0.5)
    vystrel.penup()
    vystrel.goto(hrac.xcor(), hrac.ycor())
    vystrel.dy = 20
    vystrely.append(vystrel)

screen.listen()
screen.onkey(pohyb_doleva, "a")
screen.onkey(pohyb_doprava, "d")
screen.onkey(vystrel, "space")

while True:
    screen.update()
    for objekt in padajici_objekty:
        y = objekt.ycor()
        y -= rychlost_objektu
        objekt.sety(y)

        if y < -290:
            objekt.hideturtle()
            padajici_objekty.remove(objekt)
            skore += 1
            text_skore.clear()
            text_skore.write("Skóre: {}".format(skore), align="center", font=("Courier", 24, "normal"))

    for vystrel in vystrely:
        y = vystrel.ycor()
        y += vystrel.dy
        vystrel.sety(y)

        if y > 290:
            vystrel.hideturtle()
            vystrely.remove(vystrel)

        for objekt in padajici_objekty:
            if vystrel.distance(objekt) < 30:
                objekt.hideturtle()
                padajici_objekty.remove(objekt)
                vystrel.hideturtle()
                vystrely.remove(vystrel)
                skore += 1
                text_skore.clear()
                text_skore.write("Skóre: {}".format(skore), align="center", font=("Courier", 24, "normal"))


    if random.randint(1, 1) == 1:
        objekt = turtle.Turtle()
        objekt.speed(0)
        objekt.shape("circle")
        objekt.color("black")
        a =random.uniform(0.5, 3)
        objekt.shapesize(stretch_wid=a, stretch_len = a)
        objekt.penup()
        objekt.goto(random.randint(-280, 280), 280)
        padajici_objekty.append(objekt)


    for objekt in padajici_objekty:
        if hrac.distance(objekt) < 20:
            text_skore.goto(0, 0)
            text_skore.write("Konec hry! Skóre: {}".format(skore), align="center", font=("Courier", 24, "normal"))
            znovu = textinput("chceš hrát znovu? ano/ne")
            if znovu == "ano":
                turtle.Screen()
            else:
                print("ok tak čus")
                turtle.bye()




