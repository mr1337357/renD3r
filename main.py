import time
import sys,pygame
import cube
import vector
import math

screen = pygame.display.set_mode((320,240))

srf = pygame.Surface(screen.get_size(),0,screen)

c = 0

def drawcube(pa,angle1=0.0,angle2=0.0):
    global c
    depth = {}
    rot1 = vector.matrix()
    rot1[(1,1)]=math.cos(angle1)
    rot1[(1,2)]=-math.sin(angle1)
    rot1[(2,1)]=math.sin(angle1)
    rot1[(2,2)]=math.cos(angle1)
    rot2 = vector.matrix()
    rot2[(0,0)]=math.cos(angle2)
    rot2[(2,0)]=math.sin(angle2)
    rot2[(0,2)]=-math.sin(angle2)
    rot2[(2,2)]=math.cos(angle2)

    for point in cube.cached():
        v = vector.vector(*point)
        v = v.transform(rot1)
        v = v.transform(rot2)
        v.z+=2
        r = v.rasterize()
        x = r[0]
        y = -r[1]
        z = r[2]
        x *= 100
        y *= 100
        x+=160
        y+=120
        x = int(x)
        y = int(y)
        b = 3-z
        b = int(b*100)
        if b > 255:
            b = 255
        if b < 0:
            b = 0
        
        color = pygame.Color(b,b,b)
        try:
            if depth[(x,y)] > z:
                pa[x,y]=color
                depth[(x,y)] = z
        except:
            pa[x,y]=color
            depth[(x,y)] = z

angle1=0.0
angle2=0.0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    srf.fill((0,0,0,0))
    screen.fill((0,0,0,0))
    pa = pygame.PixelArray(srf)
    drawcube(pa,angle1,angle2)
    angle1+=.05
    if angle1>6.28:
        angle1-=6.28
    angle2+=.03
    if angle2>6.28:
        angle2-=6.28
    pa = None
    screen.blit(srf,(0,0))
    pygame.display.flip()

