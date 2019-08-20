from vector import vector

class line:

    def __init__(self,start,end,points):
        self.points = []
        step = (end-start).scaled(1/float(points))
        for i in range(points):
            self.points.append(start)
            start += step
            
    def getpoints(self):
        for point in self.points:
            yield point