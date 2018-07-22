# function to draw color snake 
import turtle,time,random

def drawSnake(rad,angle,len,neckrad):
    #random color list
    colorlist = ["#800000","#FF0000","#FFB6C1","#4B0082","#FFA07A","#FFFF00","#ADFF2F"]	
    for i in range(len):
        color = colorlist[random.randint(0,6)]
        turtle.pencolor(color)
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    #drawboard postion
    turtle.setup(1300,400,0,0)
    pythonsize = 20 
    turtle.pensize(pythonsize)
    turtle.seth(-40)
    drawSnake(40,80,5,pythonsize/2)
    

main()
#wait for 3 sec
time.sleep(3)     