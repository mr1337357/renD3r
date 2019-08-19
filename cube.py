def getpoints():
    for i in range(100):
        f = float(i)
        f /= 100.0
        f -= .5

        #horizontal lines
        yield (f,.5,-.5) #top front
        yield (f,-.5,-.5) #bottom front
        yield (f,.5,.5) #top back
        yield (f,-.5,.5) #bottom back
        
        #vertical lines
        yield (-.5,f,-.5) #front left
        yield (.5,f,-.5) #front right
        yield (-.5,f,.5) #back left
        yield (.5,f,.5) #back right
        
        #away from camera
        yield (-.5,.5,f) #top left
        yield (.5,.5,f) #top right
        yield (-.5,-.5,f) #bottom left
        yield (.5,-.5,f) #bottom right

cache = None

def cached():
    global cache
    if cache == None:
        cache = [x for x in getpoints()]
    for x in cache:
        yield x
