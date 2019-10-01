import time
import sys,pygame
from cube import cube
from vector import vector
import math

elements = []

def drawobj(pa,obj):
    w = pa.surface.get_width()
    h = pa.surface.get_height()
    depth = {}
    #print dir(pa.surface)
    for point in obj.getpoints():
        loc = point.rasterize()
        x = loc[0]*w+w/2.0
        y = -loc[1]*h+h/2.0
        d = loc[2]
        x = int(x)
        y = int(y)
        if x < 0 or x > w-1:
            continue
        if y < 0 or y > h-1:
            continue
        if d <= 0:
            continue
        b = 255 - ((d-1.2) * 150)
        b = int(b)
        if b >= 255:
            continue
        try:
            if depth[(x,y)]>d:
                pa[x,y] = pygame.Color(b,b,b,255)
                depth[(x,y)]=d
        except:
            pa[x,y] = pygame.Color(b,b,b,255)
            depth[(x,y)]=d
       

def draw(pa):
    for element in elements:
        drawobj(pa,element)

if __name__ == '__main__':
    x = 0.0
    y = 0.0
    screen = pygame.display.set_mode((320,240))
    srf = pygame.Surface(screen.get_size(),0,screen)

    elements.append(cube(0.3))
    elements[0].moveto(vector(0.0,0.0,3.0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        srf.fill((0,0,0,0))
        screen.fill((0,0,0,0))
        pa = pygame.PixelArray(srf)
        elements[0].moveto(vector(math.cos(x),math.sin(x),2.0))
        x = x + .01
        y = y + .04
        elements[0].turn(vector(x,y,y*1.7))
        draw(pa)
        pa = None
        screen.blit(srf,(0,0))
        pygame.display.flip()