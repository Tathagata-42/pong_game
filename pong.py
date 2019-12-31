
import turtle #basic graphics but pygame is better
import winsound

wn=turtle.Screen()#to build the window
wn.title("Tathagata Banerjee")
wn.bgcolor("black")#to make the bavkground color black
wn.setup(width=800,height=600)
wn.tracer(0)#stops the window for updating




#scoring
score_a=0
score_b=0






#Paddle A

paddle_a=turtle.Turtle()#Turtle is the name of class hence in capital
paddle_a.speed(0)#for animation .
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()#turtles by definnation draws a line so pen up helps in not drawing a line
paddle_a.goto(-350,0)






#Paddle B

paddle_b=turtle.Turtle()#Turtle is the name of class hence in capital
paddle_b.speed(0)#for animation .
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()#turtles by definnation draws a line so pen up helps in not drawing a line
paddle_b.goto(350,0)#350 for right side







#Ball

ball=turtle.Turtle()#Turtle is the name of class hence in capital
ball.speed(0)#for animation .
ball.shape("square")
ball.color("white")

ball.penup()#turtles by definnation draws a line so pen up helps in not drawing a line
ball.goto(0,0)#for centre postion

#balls needds to move both in x direction and y direction

ball.dx=0.1
ball.dy=-0.15 #this means the that the ball moves right 2 and up 2




#pen

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B:0",align="center",font=("Courier",24,"normal"))










#Function

def paddle_a_up():
    y=paddle_a.ycor()#determines y co-ordinate
    y=y+20#adds 20 pixels to y
    paddle_a.sety(y)#sets the new value of y


def paddle_a_down():
    y=paddle_a.ycor()#determines y co-ordinate
    y=y-20#adds 20 pixels to y
    paddle_a.sety(y)#sets the new value of y


def paddle_b_up():
    y=paddle_b.ycor()#determines y co-ordinate
    y=y+20#adds 20 pixels to y
    paddle_b.sety(y)#sets the new value of y


def paddle_b_down():
    y=paddle_b.ycor()#determines y co-ordinate
    y=y-20#adds 20 pixels to y
    paddle_b.sety(y)#sets the new value of y






# Keyboard binding - present in turtle module

wn.listen()#asks to listen 
wn.onkeypress(paddle_a_up,"w")#when the user presses w the function is called 
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")#Up is used for up arrow
wn.onkeypress(paddle_b_down,"Down")




     







#Main game loop

while True:
    wn.update()#upadtes the window everytime the loop runs


    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking

    if ball.ycor()>290: #top border
        ball.sety(290)
        ball.dy=ball.dy*(-1)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        

    if ball.ycor()<-290: #bottom border
        ball.sety(-290)
        ball.dy=ball.dy*(-1)
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a=score_a+1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))
        winsound.PlaySound("score_sound",winsound.SND_ASYNC)
       

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx=ball.dx*-1
        score_b=score_b+1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Courier",24,"normal"))
        winsound.PlaySound("score_sound",winsound.SND_ASYNC)


    

    #Paddle and ball collision


    if ball.xcor() > 340 and ball.xcor()<350  and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50): # to check if the ball is touching iin the ends , top of the paddle , bottom of the paddle
       
       ball.setx(340)
       ball.dx*=-1
       winsound.PlaySound("paddle sound.wav",winsound.SND_ASYNC)


    if ball.xcor() < -340 and ball.xcor()<350  and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50): # to check if the ball is touching iin the ends , top of the paddle , bottom of the paddle
        ball.setx(-340)
        ball.dx*=-1
        winsound.PlaySound("paddle sound.wav",winsound.SND_ASYNC)




   



 

 


