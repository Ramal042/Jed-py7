import turtle
import keyboard

ninja = turtle.Turtle()

while True:
    if keyboard.is_pressed("w"):
       ninja.forward(10)

    if keyboard.is_pressed("d"):
       ninja.left(45)
    if keyboard.is_pressed("s"):   
       ninja.forward(10)

          

    if keyboard.is_pressed("b"):
       break
