from turtle import Screen,Turtle
import random


screen = Screen()
race_is_on = False
distances = [60 , 36 , 12 , -12 , -36 , -60]
colors = ["yellow" , "blue" , "red" , "green" , "orange" , "purple"]
screen.setup(width=500 , height = 400)
user_bet = screen.textinput(title="make your bet" , prompt= "Which turtle will win the race? Enter a color: ")
turtles = []

for i in range(0,6):
 t = Turtle(shape="turtle")
 t.penup()
 t.color(colors[i])
 t.goto(x = -230 , y =distances[i])
 turtles.append(t)

if user_bet:
    race_is_on = True
while race_is_on:
 for turtle in turtles:
  if t.xcor()>=230:
      winner = t.pencolor()
      race_is_on=False
      if winner == user_bet:
          print(f"You've win! {winner} color turtle won the race.")
      else:
          print(f"You've lost! {winner} color turtle won the race.")


  random_distance = turtle.forward(random.randint(0,10))






# def move_forward():
#     pen.forward(10)
#
# def move_backward():
#     pen.backward(10)
# def move_clockwise():
#     pen.circle(50, 10)
# def move_counterclock():
#     pen.circle(-50,10)
# def clear():
#     pen.penup()
#     pen.clear()
#     pen.home()
#     pen.pendown()
#
# screen.listen()
# screen.onkey(key = "a" , fun=move_counterclock)
# screen.onkey(key = "d" , fun=move_clockwise)
# screen.onkey(key = "w" , fun=move_forward)
# screen.onkey(key = "s" , fun=move_backward)
# screen.onkey(key = "c" , fun=clear)

screen.exitonclick()