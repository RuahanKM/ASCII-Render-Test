HighScore = 0

while True:
    import keyboard as k
    import time
    import random as ra

    print("Press space to start")
    k.wait('space')

    maxHeight = 10
    minHeight = -10
    width = 60
    padding = 30
    speed = 30
    xPos = 5.0
    grav = -45
    pipex = 100
    PipeCenter = 0
    PipeSize = 4
    jumpHeight = 16
    termVel = -4
    debug = True
    FPS = 0



    ySpeed = 0
    lastFrameTime = time.time()
    points = [(xPos,0.0)]
    playing = True
    score = 0
    canScore = True

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
            debugInfo = "pos: " + str(points[0]) + "\n" + "vel: " + str(ySpeed)
            print("\r" + (('\n'*padding) + debugInfo + "\n" + ("Score: " + str(score)+ "\n") + finalString), end="")
        else:
            # https://stackoverflow.com/questions/465348/how-can-i-overwrite-print-over-the-current-line-in-windows-command-line
            print("\r" + (('\n'*padding) + ("Score: " + str(score) + "\n") + finalString), end="")


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

    def line(x, y, b):
        global points
        add_points = []
        if b:
            for i in range(minHeight, y):
                add_points.append((x, i))
        else:
            for i in range(maxHeight, y, -1):
                add_points.append((x, i))
        return add_points

    def pipe(s, c, x):
        return line(x, int(c - s / 2), True) + line(x, int(c + s / 2), False)

    def GameOver():
        global playing
        global HighScore

        playing = False
        print("Game Over!\n")

        if score > HighScore:
            HighScore = score
            print("New high score!")

        print("Score: " + str(score))
        print("High score: " + str(HighScore) + "\n")

    def Score():
        global score
        global canScore
        if canScore:
            score += 1
            canScore = False
    def main(deltatime):
        global ySpeed
        global points
        global pipex
        global PipeCenter
        global canScore

        points[0] = AddTuple(points[0], 0, 0.5 * ySpeed * deltatime)

        if k.is_pressed('space'):
            ySpeed = jumpHeight

        ySpeed += grav * deltatime

        points[0] = AddTuple(points[0], 0, 0.5 * ySpeed * deltatime)

        pipex -= speed * deltatime
        pipeInstince = pipe(PipeSize, PipeCenter, int(pipex))
        points += pipeInstince

        if pipex <= 0:
            canScore = True
            pipex = width + 1
            PipeCenter = ra.randint(minHeight + PipeSize, maxHeight-PipeSize)
        if int(pipex) == xPos:
            Score()

        render(points)

        for i in pipeInstince:
            if int(i[0]) == int(points[0][0]) and int(i[1]) == int(points[0][1]):
                GameOver()

            points.remove(i)

        if points[0][1] >= maxHeight:
            points[0] = SetTuple(points[0], xPos, maxHeight)

        if points[0][1] <= minHeight:
            GameOver()




    while playing:
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

    time.sleep(1)