import math
class matrix:
    def __init__(self,values=None):
        if values == None:
            values = [1,0,0,0,1,0,0,0,1]
        self.values = values
    def __getitem__(self,index):
        try:
            return self.values[index[0]+index[1]*3]
        except:
            return self.values[index]
    def __setitem__(self,index,value):
        try:
            self.values[index[0]+index[1]*3] = value
        except:
            self.values[index] = value
    def __str__(self):
        out = '[{},{},{}]\n[{},{},{}]\n[{},{},{}]\n'.format(*self.values)
        return out


class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

    def topolar(self):
        r = math.sqrt(x*x+y*y+z*z)
        a = math.atan(self.y/self.x)
        e = math.atan(self.z/self.x)

    def transform(self,matrix):
        x = self.x*matrix[(0,0)]+self.y*matrix[(0,1)]+self.z*matrix[(0,2)]
        y = self.x*matrix[(1,0)]+self.y*matrix[(1,1)]+self.z*matrix[(1,2)]
        z = self.x*matrix[(2,0)]+self.y*matrix[(2,1)]+self.z*matrix[(2,2)]
        return vector(x,y,z)

    def rasterize(self):
        if self.z <= 0:
            return (-1,-1)
        d = math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        return (self.x/self.z,self.y/self.z,d)
