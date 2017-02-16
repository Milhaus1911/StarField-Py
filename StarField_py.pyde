#Layton Wright
#16/02/2017
#Python version of the StarField processing code written by Daniel Shiffman.
#https://github.com/CodingTrain/Rainbow-Code/tree/master/challenges/CC_01_StarField

from star import Star

#Set variables
stars = []
speed = 1.0
play = True

def setup():
    size(800,800)
    #Fill the array stars with Stars, using the Star() class.
    [stars.append(Star(width, height)) for i in range(800)]
            
def draw():
    #Link the speed variable to the mouse position.
    speed = map(mouseX, 0, width, 0, 100)
    background(0)
    #Move the center to the middle of the window.
    translate(width/2, height/2)
    #Draw each star in the array. The update() method updates the stars position
    #and show() displays it on the canvas.
    for i in range(len(stars)):
        stars[i].update(speed)
        stars[i].show()
    
        
def mouseClicked():
    #Pauses the animation when the mouse is clicked in the window.
    global play
    if play:
        noLoop()
        play = False
    else:
        loop()
        play = True

    