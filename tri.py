class triangle:
    #define a triangle with points sorted by height
    def __init__(self,top,mid,bot,texture = None): #topmost point,middle point, bottom point, texture
        self.top = top
        self.mid = mid
        self.bot = bot
        self.texture = texture
        self.points = None
    
    def generate_points(self,w,h):
        pass