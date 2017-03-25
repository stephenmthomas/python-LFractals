import pygame, math
from random import randint

running = 1
width = 1600
height = 1000
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0, 255)
red1, red2 = 100, 25
grn1, grn2 = 10, 90
blu1, blu2 = 5, 25


xo, yo = 500, 700

ticker = 10
antialias = 1
angle = -90
branch = 20
scale = 0.75
size = 100
colordex = []
depth = 10
depthlim = 100
lean = 0
chaos = 0
fchaos = 0

def colorfade(r1, g1, b1, r2, g2, b2, steps):
    global colordex
    colordex = []
    rstep = (r2 - r1) / steps
    gstep = (g2 - g1) / steps
    bstep = (b2 - b1) / steps

    for i in range(steps + 1):
        newcolor = (r1 + rstep * i, g1 + gstep * i, b1 + bstep * i)
        colordex.append(newcolor)


def drawTree(x1, y1, size, angle, depth):
    global colordex
    if depth >= 0.9 * depth:
        fchaos = randint(chaos *-1, chaos)
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle + 0.05 * fchaos)) * (size + depth))
        y2 = y1 + int(math.sin(math.radians(angle + 0.25 * fchaos)) * (size + depth))
        if antialias == 1: pygame.draw.aaline(screen, colordex[depth], (x1, y1), (x2, y2), 2)
        if antialias == 0: pygame.draw.line(screen, colordex[depth], (x1, y1), (x2, y2), 2)
        drawTree(x2, y2, size * scale, angle - branch + lean, depth - 1)
        drawTree(x2, y2, size * scale, angle + branch + lean, depth - 1)

def drawshapes():
    screen.fill((BLACK))
    drawTree(xo, yo, size, angle, depth)

screen = pygame.display.set_mode((width, height))
screen.fill((BLACK))
colorfade(red1,grn1,blu1,red2,grn2,blu2,depth)

#MAINLOOP
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            #prints values for branch, scale, size, depth, lean
            print "Branch: %d" % branch
            print "Scale: %d" % scale
            print "Size: %d" % size
            print "Lean: %d" % lean
            print "Depth: %d" % depth
            print "RGB1: %d %d %d" % (red1, grn1, blu1)
            print "RGB2: %d %d %d" % (red2, grn2, blu2)


        if event.key == pygame.K_0:
            if antialias == 0: antialias = 1
            else: antialias = 0
        if event.key == pygame.K_z:
            depth += 1
            if depth == depthlim: depth -= 1
            colorfade(red1,grn1,blu1,red2,grn2,blu2,depth)
        if event.key == pygame.K_x:
            depth -= 1
            if depth == 0: depth = 1
            colorfade(red1,grn1,blu1,red2,grn2,blu2,depth)

    move_ticker = 0
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if move_ticker == 0:
            move_ticker = ticker
            branch += 1
            if branch == 360 or branch == -360: branch = 0
    if keys[pygame.K_RIGHT]:
        if move_ticker == 0:
            move_ticker = ticker
            branch -= 1
            if branch == 360 or branch == -360: branch = 0
    if keys[pygame.K_UP]:
        if move_ticker == 0:
            move_ticker = ticker
            scale += 0.01
    if keys[pygame.K_DOWN]:
        if move_ticker == 0:
            move_ticker = ticker
            scale -= 0.01
    if keys[pygame.K_a]:
        if move_ticker ==0:
            move_ticker = ticker
            size += 1
    if keys[pygame.K_s]:
        if move_ticker ==0:
            move_ticker = ticker
            size -= 1
    if keys[pygame.K_r]:
        if move_ticker ==0:
            move_ticker = ticker
            red1 += 1
            if red1 >= 255:
                red1 = 0
            colorfade(red1,grn1,blu1,red2,grn2,blu2,depth)
    if keys[pygame.K_g]:
        if move_ticker ==0:
            move_ticker = ticker
            grn1 += 1
            if grn1 >= 255:
                grn1 = 0
            colorfade(red1,grn1,blu1,red2,grn2,blu2,depth)
    if keys[pygame.K_b]:
        if move_ticker ==0:
            move_ticker = ticker
            blu1 += 1
            if blu1 >= 255:
                blu1 = 0
            colorfade(red1,grn1,blu1,red2,grn2,blu2,depth)
    if keys[pygame.K_t]:
        if move_ticker ==0:
            move_ticker = ticker
            red2 += 1
            if red2 >= 255:
                red2 = red1
            colorfade(red1,grn1,blu1,red2,grn2,blu2,depth)
    if keys[pygame.K_h]:
        if move_ticker ==0:
            move_ticker = ticker
            grn2 += 1
            if grn2 >= 255:
                grn2 = grn1
            colorfade(red1,grn1,blu1,red2,grn2,blu2,depth)
    if keys[pygame.K_n]:
        if move_ticker ==0:
            move_ticker = ticker
            blu2 += 1
            if blu2 >= 255:
                blu2 = blu1
            colorfade(red1,grn1,blu1,red2,grn2,blu2,depth)

    if keys[pygame.K_q]:
        lean += 1
    if keys[pygame.K_w]:
        lean -= 1

    if keys[pygame.K_c]:
        chaos += 1

    if keys[pygame.K_v]:
        chaos = 0

    if move_ticker > 0:
        move_ticker -= 1

    drawshapes()
    pygame.display.update()
    fpsClock.tick(FPS)