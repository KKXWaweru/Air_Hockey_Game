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

#Hockey Puck movement
puck.dx = 0.1
puck.dy = -0.1


#Paddle Movement
#Player 1 Controls 
def paddle1_up():
    y = paddle1.ycor()        #This specifies the current position of the paddle and setting it to y
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()        #This specifies the current position of the paddle and setting it to y
    y -= 20
    paddle1.sety(y)

#Player 2 Controls
def paddle2_up():
    y = paddle2.ycor()        #This specifies the current position of the paddle and setting it to y
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()        #This specifies the current position of the paddle and setting it to y
    y -= 20
    paddle2.sety(y)

#Binding the keyboard to the paddles
wn.listen()
wn.onkeypress(paddle1_up, "w") #Bound player 1's controls to w and s (NO CAPS)
wn.onkeypress(paddle1_down,"s")

wn.onkeypress(paddle2_up,"Up")
wn.onkeypress(paddle2_down,"Down")
#Main Air hockey game component
while True:
    wn.update()

    #Puck Movement
    puck.setx(puck.xcor() + puck.dx)
    puck.sety(puck.ycor() + puck.dy)

    #Setting the game limits and ensure the paddles and the ball don't exceed the window
    #Top of the window
    if puck.ycor() > 290:
        puck.sety(290)
        puck.dy *= -1  #The -1 reverses the direction in which the ball is moving 

    #Bottom of the window
    if puck.ycor() < -290:
        puck.sety(-290)
        puck.dy *= -1     

    #Creating goal instances
    #Player 1 goal
    if puck.xcor() > 390:
        puck.goto(0,0)
        puck.dx *= -1

    #Player 2 goal
    if puck.xcor() <-390:
        puck.goto(0,0)
        puck.dx *= -1
