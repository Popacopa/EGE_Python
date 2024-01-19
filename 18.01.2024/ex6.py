from turtle import *


def filt(arg):
  x, y = arg
  if str(x).split('.')[1][0] == '0' or str(y).split('.')[1][0] == '0':
    return True 
  else:       #Ответ правильный только в том случае, когда хотя бы одна координата - целое число (хз)
    return False
  
turtle = Turtle()

cache = []

turtle.goto(0, 0)
for steps in range(8):
  turtle.right(45)              
  for i in range(8):
    turtle.forward(1)
    cache.append((turtle.xcor(), turtle.ycor()))


cache = list(filter(filt, cache))

print(len(cache)) 
 


  





