class myclass:
    msg='hi'
    def __init__(self):
        print(self.msg)
    def fun(self):
        print("message is ",self.msg)
s=myclass()
s.fun()

class student:
    def __init__(self):
        print("welcome")
    def show(self,name):
        print("hello",name)
s1=student()
s1.show('guna')

class employee:
    def __init__(self,na,tk):
        self.name=na
        self.tocken=tk
    def display(self):
        print('name : ',self.name)
        print("tocken no : ",self.tocken)
e1=employee('guna',15)
e2=employee('hari',18)
e1.display()
e2.display()

class admin:
    c=0
    def __init__(self):
        admin.c+=1
        print("no of student is ",admin.c)
a1=admin()
a2=admin()
a3=admin()
a4=admin()

def fun():
    print("welcome")
class sun:
    f=fun()
c=sun()


class calc:
    def add(self,a,b):
        print(a+b)
class calc1(calc):
    def multi(self,a,b):
        print(a*b)
class calc2(calc1):
    def div(self,a,b):
        print(a//b , a%b)
class calc3(calc2):
    def sub(self,a,b):
        print(a-b)
c3=calc3()
c3.add(2,5)
c3.sub(5,2)
c3.multi(4,1)
c3.div(8,3)

class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __add__(self,o):
        x=self.x+o.x
        y=self.y+o.y
        return point(x,y)
    def __str__(self):
        return f'{self.x},{self.y}'
p1=point(2,5)
p2=point(3,6)
p3=p1+p2
print(p3)

class dist:
    def __init__(self,f,i):
        self.feet=f
        self.inch=i
        
    def __add__(a,b):
        i=a.inch+b.inch
        f=a.feet+b.feet
        if(i>=12):
            i-=12
            f+=1
            if(i>=12):
                i-=12
                f+=1
        return dist(f,i)
    def show(self):
        print(f'feet={self.feet}  inches={self.inch}')
a,b=input('entre two number :').split()
a=int(a);b=int(b)
c,d=input("enter second two number :").split()
c=int(c);d=int(d)
d1=dist(a,b)
d2=dist(c,d)
d3=d1+d2
d3.show()
