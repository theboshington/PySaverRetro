import pygame
import random
import math
pygame.init()

dispw = 1920
disph = 1080

fin = 0

w = int(dispw/2)
h = int(disph/2)

gameDisplay = pygame.display.set_mode((dispw, disph),  pygame.FULLSCREEN)

clock = pygame.time.Clock()
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)


def colour_change(c):

    x = []
    for i in c:
        x.append(i)

    if x[0] > 0 and x[1] == 255 and x[2] == 255:
        x[0] -= 1
    elif x[0] == 0 and x[1] > 0 and x[2] == 255:
        x[1] -= 1
    elif x[0] == 0 and x[1] == 0 and x[2] > 0:
        x[2] -= 1
    elif x[0] < 255 and x[1] == 0 and x[2] == 0:
        x[0] += 1
    elif x[0] == 255 and x[1] < 255 and x[2] == 0:
        x[1] += 1
    elif x[0] == 255 and x[1] == 255 and x[2] < 255:
        x[2] += 1

    newtup = (x[0], x[1], x[2])

    return newtup


def loop():
    global gameDisplay
    global w
    global h
    n = 1
    c = 0
    count2 = 0
    spiral = 1
    colour_phase = (255, 255, 255)
    colour_antiphase = (0, 0, 0)
    colour_otherphase = (0, 122, 255)
    square = 1
    circle = 0
    first = 1
    movement = 0
    while not fin:
        randomtime = random.randint(0, 5000)

        if randomtime == 1 or randomtime == 2 or randomtime == 3 or first == 1:
            gameDisplay.fill(black)
            square = random.choice([0, 1])
            spiral = random.choice([0, 1])
            circle = random.choice([0, 1])
            movement = random.choice([0, 1])
            first = 0

        while (square == 1 and spiral == 1 and circle == 1) \
                or (square == 0 and spiral == 0 and circle == 0)\
                or (square == 1 and circle == 1)\
                or (square == 1 and spiral == 1):

            square = random.choice([0, 1])
            spiral = random.choice([0, 1])
            circle = random.choice([0, 1])

        
        if movement == 0:
            w = dispw/2
            h = disph/2

        point_list_two = []
        point_list_three = []
        point_list = getfiblist(n)

        for each in point_list:

            point_list_two.append(((each[0] + 1), (each[1] + 1)))
            point_list_three.append(((each[0] - 1), (each[1] - 1)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                pygame.quit()
                quit()
                
        if square == 1:
            sqlist = [((w - (w*n)), (h - (h*n))),
                      (w - (w*n), h + (h*n)),
                      (w + (w*n), h + (h*n)),
                      (w + (w*n), h - (h*n))]

            sqlist2 = [((w - (w*n/4)), (h - (h*n/4))),
                       ((w - (w*n/4)), (h + (h*n/4))),
                       ((w + (w*n/4)), (h + (h*n/4))),
                       ((w + (w*n/4)), (h - (h*n/4)))]
            
            sqlist3 = [((w - (w*n*1.5)), (h - (h*n*1.5))),
                       ((w - (w*n*1.5)), (h + (h*n*1.5))),
                       ((w + (w*n*1.5)), (h + (h*n*1.5))),
                       ((w + (w*n*1.5)), (h - (h*n*1.5)))]
            
            pygame.draw.polygon(gameDisplay, colour_otherphase, sqlist, 15)
            pygame.draw.polygon(gameDisplay, colour_otherphase, sqlist2, 15)
            pygame.draw.polygon(gameDisplay, colour_otherphase, sqlist3, 25)
            print(sqlist)
            print(colour_otherphase)

        if spiral == 1:

            pygame.draw.lines(gameDisplay, colour_phase, False, point_list, 25)

        if circle == 1:
            for each in point_list:

                count2 += 1
                if getfib(count2) < 2*w:

                    pygame.draw.circle(gameDisplay, colour_antiphase, each, math.floor(getfib(count2)*n), 0)
            count2 = 0
        
        if 0.1485 < n <= 1:
            n *= 0.989
        elif n <= 0.1485:
            n = 1

        if movement == 1:
            rand_num = random.choice([1, 2])
            if rand_num == 1:
                w += random.choice([2, -2])
            elif rand_num == 2:
                h += random.choice([2, -2])

        pygame.display.update()
        colour_phase = colour_change(colour_phase)
        colour_antiphase = colour_change(colour_antiphase)
        colour_otherphase = colour_change(colour_otherphase)

        clock.tick(120)

        c += 1


def getfiblist(n):
    newl = []
    it = 1
    c = 1
    while getfib(c)*0.1 < w:

        y = 1

        if getfib(c) == 0:
            it += 1
            y = 0

        elif it == 1:
            z = ((getfib(c)*n + w), (getfib(c)*n + h))
            it += 1

        elif it == 2:
            z = ((-getfib(c)*n + w), (getfib(c)*n + h))
            it += 1

        elif it == 3:
            z = ((-getfib(c)*n + w), (-getfib(c)*n + h))
            it += 1

        elif it == 4:
            z = ((getfib(c)*n + w), (-getfib(c)*n + h))
            it = 1

        else:
            it == 1

        c += 1

        if y == 1:
            newl.append(((int(z[0])), (int(z[1]))))
    return newl


def getfib(nth):
    x = 0
    y = 1
    fib = []
    it = 0
    hasamend = 0
    c = 0
    while c < nth:
        if hasamend == 0:
            fib.append(0)
            fib.append(1)
            hasamend = 1
        if it == 0:
            x += y
            fib.append(x)
            it = 1
        elif it == 1:
            y += x
            fib.append(y)
            it = 0
        c += 1
    return fib[(nth - 1)]

loop()
