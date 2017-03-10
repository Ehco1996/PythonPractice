# function to draw snake 
import turtle,time

def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    #zhixianpaxing 
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    #drawboard postion
    turtle.setup(1300,800,0,0)
    pythonsize = 30 
    turtle.pensize(pythonsize)
    turtle.pencolor("blue")
    turtle.seth(-40)
    drawSnake(40,80,2,pythonsize/2)
    

main()
#wait for 3 sec
time.sleep(3)     