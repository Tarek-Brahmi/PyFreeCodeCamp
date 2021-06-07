class Rectangle:
    def __init__(self,width=None,height=None) -> None:
        self.height=height
        self.width=width
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return self.height*self.width
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    def get_picture(self):
        x=""
        for i in range(self.height):
            x+="*"*self.width
            x+='\n'
        return str(x)
    
    def get_amount_inside(self,other):
        return self.get_area()//other.get_area()
    def __repr__(self):
        return '%s(width=%d,height=%d)'%(self.__class__.__name__,self.width,self.height)
class Square(Rectangle):
    def __init__(self, side) -> None:
        Rectangle.__init__(self,width=side, height=side)
        self.side=side
    def set_side(self,side):
        self.side=side
    def __repr__(self):
        return "%s(side=%d)"%(self.__class__.__name__,self.side)
    def get_area(self):
        return self.side**2
    def get_picture(self):
        x=""
        for i in range(self.side):
            x+="*"*self.side
            x+='\n'
        return str(x)