#Create card with TEXT
import turtle
t1=turtle.Turtle()
t1.width(10)
t1.color("blue")
t1.forward(300)
t1.left(90)
t1.forward(300)
t1.left(90)
t1.forward(300)
t1.left(90)
t1.forward(300)
t1.penup()
t1.goto(30, 250)
t1.left(90)
t1.color("black")
t1.write("Name: Jamal", font=('tahoma', 12))
t1.penup
t1.goto(30,200)
t1.write("Last Name: Azizbeigi", font=('impact',15))
t1.penup()
t1.goto(30, 150)
t1.write("My code is: 123", font=('arial', 20))

