from vector import vector,matrix
from line import line

class cube:
    def __init__(self,size):
        self.size = size
        #vertices
        self.vertices = []
        for i in range(8):
            if i & 1 == 0:
                x = size/2
            else:
                x = -size/2
                
            if i & 2 == 0:
                y = size/2
            else:
                y = -size/2
                
            if i & 4 == 0:
                z = size/2
            else:
                z = -size/2
            self.vertices.append(vector(x,y,z))
        
        self.loc = vector()
        self.angles = vector()

    def moveto(self,loc):
        self.loc = loc
    
    def turn(self,angle):
        self.angles = angle

    def getpoints(self):
        mtx = matrix()
        mtx.translate(self.loc)
        mtx.rotatex(self.angles.x)
        mtx.rotatey(self.angles.y)
        mtx.rotatez(self.angles.z)
        tatered = []
        for vertex in self.vertices:
            tatered.append(vertex.transform(mtx))
        
        for p,q in zip(line(tatered[0],tatered[1],50).getpoints(),line(tatered[2],tatered[3],50).getpoints()):
            for r in line(p,q,50).getpoints():
                yield r
        for p,q in zip(line(tatered[4],tatered[5],50).getpoints(),line(tatered[6],tatered[7],50).getpoints()):
            for r in line(p,q,50).getpoints():
                yield r
        
        for p,q in zip(line(tatered[0],tatered[1],50).getpoints(),line(tatered[4],tatered[5],50).getpoints()):
            for r in line(p,q,50).getpoints():
                yield r
        for p,q in zip(line(tatered[2],tatered[3],50).getpoints(),line(tatered[6],tatered[7],50).getpoints()):
            for r in line(p,q,50).getpoints():
                yield r

        for p,q in zip(line(tatered[0],tatered[2],50).getpoints(),line(tatered[4],tatered[6],50).getpoints()):
            for r in line(p,q,50).getpoints():
                yield r
        for p,q in zip(line(tatered[1],tatered[3],50).getpoints(),line(tatered[5],tatered[7],50).getpoints()):
            for r in line(p,q,50).getpoints():
                yield r

        for v in self.vertices:
            yield v.transform(mtx)