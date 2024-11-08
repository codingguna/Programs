def fun(x,y):
    print("x=",x,"y=",y)
    
class ex:
    def f(self,x,y):
        fun(x, y)

x=ex()
x.f(2,4)