import math
class matrix:
    def __init__(self,values=None):
        if values == None:
            values = [1.0,0.0,0.0,0.0,
                      0.0,1.0,0.0,0.0,
                      0.0,0.0,1.0,0.0,
                      0.0,0.0,0.0,1.0]
        self.values = values
        
    def __getitem__(self,index):
        try:
            return self.values[index[0]+index[1]*4]
        except:
            return self.values[index]
            
    def __setitem__(self,index,value):
        try:
            self.values[index[0]+index[1]*4] = value
        except:
            self.values[index] = value
            
    def composed(self,other):
        m = matrix()
        for i in range(4):
            for j in range(4):
                m[(j,i)]=self[(0,i)]*other[(j,0)]+self[(1,i)]*other[(j,1)]+self[(2,i)]*other[(j,2)]+self[(3,i)]*other[(j,3)]
        return m
        
    def translate(self,location):
        self[(3,0)] = location.x
        self[(3,1)] = location.y
        self[(3,2)] = location.z
    
    def rotatex(self,angle):
        n = matrix()
        n[(1,1)]=math.cos(angle)
        n[(1,2)]=math.sin(angle)
        n[(2,1)]=-math.sin(angle)
        n[(2,2)]=math.cos(angle)
        self.values = self.composed(n).values
    
    def rotatey(self,angle):
        n = matrix()
        n[(0,0)]=math.cos(angle)
        n[(0,2)]=-math.sin(angle)
        n[(2,0)]=math.sin(angle)
        n[(2,2)]=math.cos(angle)
        self.values = self.composed(n).values
        
    def rotatez(self,angle):
        n = matrix()
        n[(0,0)]=math.cos(angle)
        n[(0,1)]=math.sin(angle)
        n[(1,0)]=-math.sin(angle)
        n[(1,1)]=math.cos(angle)
        self.values = self.composed(n).values
        
    def __str__(self):
        out = '[{},{},{},{}]\n[{},{},{},{}]\n[{},{},{},{}]\n[{},{},{},{}]\n'.format(*self.values)
        return out

class vector:
    def __init__(self,x=0,y=0,z=0,color=0):
        self.x=x
        self.y=y
        self.z=z
        self.color = color

    def topolar(self):
        r = math.sqrt(x*x+y*y+z*z)
        a = math.atan(self.y/self.x)
        e = math.atan(self.z/self.x)

    def transform(self,matrix):
        x = self.x*matrix[(0,0)]+self.y*matrix[(1,0)]+self.z*matrix[(2,0)]+1*matrix[(3,0)]
        y = self.x*matrix[(0,1)]+self.y*matrix[(1,1)]+self.z*matrix[(2,1)]+1*matrix[(3,1)]
        z = self.x*matrix[(0,2)]+self.y*matrix[(1,2)]+self.z*matrix[(2,2)]+1*matrix[(3,2)]
        #_ = self.x*matrix[(3,0)]+self.y*matrix[(3,1)]+self.z*matrix[(3,2)]+1*matrix[(3,3)] #unnecessary output value thrown away
        return vector(x,y,z)

    def rasterize(self):
        if self.z <= 0:
            return (-1,-1)
        d = math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        return (self.x/self.z,self.y/self.z,d)
    
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y,self.z+other.z)
        
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y,self.z-other.z)
        
    def scaled(self,factor):
        return vector(self.x*factor,self.y*factor,self.z*factor)
        
    def __str__(self):
        out = 'Vector: {},{},{}'.format(self.x,self.y,self.z)
        return out
        
if __name__ == '__main__':
    m = matrix()
    m.translate(vector(0.0,0.0,4.0))
    print m
    v = vector(0.5,0.5,0.5)
    print v.transform(m)