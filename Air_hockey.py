import turtle


wn = turtle.Screen()
wn.title("Air Hockey")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)  #prevent the window from updating

#Player 1 paddle
paddle1= turtle.Turtle()
paddle1.speed(0) #Set max speed for the animation
paddle1.shape("square")
paddle1.color("red")

paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)


#Player 2 paddle
paddle2= turtle.Turtle()
paddle2.speed(0) #Set max speed for the animation
paddle2.shape("square")
paddle2.color("blue")

paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)

#Hockey puck
puck= turtle.Turtle()
puck.speed(0) #Set max speed for the animation
puck.shape("circle")
puck.color("white")

puck.shapesize(stretch_len=1.2, stretch_wid=1.2)
puck.penup()
puck.goto(0,0)



#Main Air hockey game component
while True:
    wn.update()