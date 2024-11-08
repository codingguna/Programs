class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __add__(self,o):
        x=self.x+o.x
        y=self.y+o.y
        return point(x,y)
    def __str__(self):
        print(f'{self.x},{self.y}')
p1=point(2,5)
p2=point(3,6)
p3=p1+p2
print(p3)
