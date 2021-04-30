import keyboard as k
import time

maxHeight = 10
minHeight = -10
width = 100
padding = 100
speed = 20
debug = False
FPS = 50



lastFrameTime = 0
points = [(0.0,0.0), (10.0, 10,0)]
pad = ""
for j in range(padding):
    pad += "\n"


def render(pl):
    finalString = ""
    for y in range(maxHeight, minHeight, -1):
        curLine = ""
        for x in range(width):
            curChar = "o"
            for l in pl:
                #if the current point in the loops chords match the chords of the render loop, we add a "#", else a "."
                if int(l[0]) == x and int(l[1]) == y:
                    curChar = "#"
                    break
                else:
                    curChar = "."
            curLine += curChar
        finalString += (curLine + "\n")
    if debug:
        print(pad+finalString+str(points[0]))
    else:
        print(pad + finalString)

def AddTuple(t, x, y):
    #tuple is imutable so we have to convert it into a list first
    t = list(t)
    t[0] += x
    t[1] += y
    return tuple(t)


def main(deltatime):
    if k.is_pressed('w'):
        points[0] = AddTuple(points[0], 0, speed*deltatime)
    if k.is_pressed('s'):
        points[0] = AddTuple(points[0], 0, -speed*deltatime)
    if k.is_pressed('a'):
        points[0] = AddTuple(points[0], -speed*deltatime, 0)
    if k.is_pressed('d'):
        points[0] = AddTuple(points[0], speed*deltatime, 0)

    render(points)


while True:
    #gets deltatime
    currentTime = time.time()
    dt = currentTime - lastFrameTime

    #limits fps
    if FPS > 0:
        sleepTime = 1. / FPS - (currentTime - lastFrameTime)
        if sleepTime > 0:
            time.sleep(sleepTime)

    lastFrameTime = currentTime

    #calls main function
    main(dt)

    #prints fps
    if debug:
        try:
            CurrentFps = 1 / (time.time() - currentTime)
            print(CurrentFps)
        except ZeroDivisionError:
            print('Divide by 0')