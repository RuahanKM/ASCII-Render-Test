import keyboard as k
import time

maxHeight = 10
minHeight = -10
width = 100
padding = 30
speed = 20
grav = -8
jumpHeight = 8
termVel = -4
debug = False
FPS = 30



ySpeed = 0
lastFrameTime = time.time()
points = [(5.0,0.0)]

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
        print("\r" + (('\n'*padding)+finalString + str(points[0])), end="")
    else:
        # https://stackoverflow.com/questions/465348/how-can-i-overwrite-print-over-the-current-line-in-windows-command-line
        print("\r" + (('\n'*padding)+finalString), end="")


def AddTuple(t, x, y):
    #tuple is imutable so we have to convert it into a list first
    t = list(t)
    t[0] += x
    t[1] += y
    return tuple(t)
def SetTuple(t, x, y):
    t = list(t)
    t[0] = x
    t[1] = y
    return tuple(t)

def main(deltatime):
    global ySpeed

    points[0] = AddTuple(points[0], 0, 0.5 * ySpeed * deltatime)

    if k.is_pressed('space'):
        ySpeed = jumpHeight

    ySpeed += grav * deltatime

    points[0] = AddTuple(points[0], 0, 0.5 * ySpeed * deltatime)
    render(points)


while True:
    #gets deltatime
    currentTime = time.time()
    dt = currentTime - lastFrameTime

    #limits fps
    if FPS != 0:
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