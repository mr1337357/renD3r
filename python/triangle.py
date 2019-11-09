from vector import vector
from line import line
class triangle:
    def __init__(self):
        self.points = []
        self.points.append(vector())
        self.points.append(vector())
        self.points.append(vector())
    def fill():
        toppoint = None
        botpoint = None
        if self.points[0].y <= self.points[1].y:
            if self.points[0].y <= self.points[2].y:
                botpoint = self.points[0]
            else:
                botpoint = self.points[2]
        elif self.points[1].y <= self.ponts[2].y:
            botpoint = self.points[1]
        else:
            botpoint = self.points[2]
        
        if self.points[0].y >= self.points[1].y:
            if self.points[0].y >= self.points[2].y:
                toppoint = self.points[0]
            else:
                toppoint = self.points[2]
        elif self.points[1].y >= self.ponts[2].y:
            toppoint = self.points[1]
        else:
            toppoint = self.points[2]
        
        side = line(self.points[0],self.points[1],100)
        