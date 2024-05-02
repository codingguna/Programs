'''#1
class petrol:
    def __init__(self):
        self.liters=0
        self.price=0
    def getdetail(self,p,l):
        self.price=p
        self.liters=l
        
    def show(self):
        bill=self.liters*self.price
        print(f'your bill for {self.liters} liter of petrol is {bill:.2f}')
p=float(input("enter the amount of one liter :"))
b1=petrol()
l1=int(input("enter number of liters :"))
b1.getdetail(p,l1)
b1.show()
b2=petrol()
l=int(input("enter the number of liters :"))
b2.getdetail(p,l)
b2.show()
b3=petrol()
l2=int(input("entre the number of liters :"))
b3.getdetail(p,l2)
b3.show()

#2
class student:
    def getdetail(self,nm,rl,mk):
        self.name=nm
        self.roll=rl
        self.marks=mk
    def show(self):
        print(f'{self.name}\t\t{self.roll}\t\t{self.marks}')
print("Name \t\tRoll \t\tMark")
s1=student()
s1.getdetail("guna",15,95)
s1.show()
s2=student()
s2.getdetail('hari', 18,93)
s2.show()
s3=student()
s3.getdetail('inba', 14,89)
s3.show()
s4=student()
s4.getdetail('dharnesh',78,88)
s4.show()

#3
class Student:
    roll =2238010000
    s_no =0
    def __init__(self, name):
        self.name = name
        Student.roll+=1
        Student.s_no+= 1
    def display_info(self):
        print(f"Serial Number: {Student.s_no}")
        print(f"Name: {self.name}")
        print(f"Roll Number: {Student.roll}\n")
student1 = Student("guna")
student1.display_info()
student2 = Student("hari")
student2.display_info()

#4
import math
class dict:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist1(self):
        return(math.sqrt(self.x**2 + self.y**2))
    def dist2(self, other):
        return(math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2))
point1 = dict(3, 4)
dist_from_origin = point1.dist1()
print(f"Distance from origin: {dist_from_origin:.2f}")
point2 = dict(8,9)
dist_bet_two_point = point1.dist2(point2)
print(f"Distance between two points: {dist_bet_two_point:.2f}")

#5
class User:
    login_attempts=0
    def __init__(self, first_name, last_name, roll, age):
        self.first_name = first_name
        self.last_name = last_name
        self.roll =roll
        self.age = age
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        print(f"Roll: {self.roll}")
        print(f"Age: {self.age}")
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!\n")
    def increment_login_attempts(self):
        User.login_attempts += 1
    def reset_login_attempts(self):
        User.login_attempts = 0

user1 = User("Hari", "Dass", 18, 21)
user2 = User("Guna", "Sekar", 15, 20)
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user2.describe_user()
user2.greet_user()
user2.increment_login_attempts()
print(f"Login attempts: {User.login_attempts}")
user2.reset_login_attempts()
print(f"Login attempts: {User.login_attempts}")

#6
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, nm, ag, de, sa):
        super().__init__(nm, ag)
        self.designation = de
        self.salary = sa
    def details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Designation: {self.designation}")
        print(f"Salary: {self.salary}\n")
employee1 = Employee("Hari", 21, "Software Engineer",100000)
employee1.details()
employee2 = Employee("Dharnesh", 20, "IB Branch Manager",90000)
employee2.details()

#7
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student:
    def __init__(self, id, room_no):
        self.id = id
        self.room_number = room_no
class Resident(Person, Student):
    def __init__(self, name, age, id, room):
        Person.__init__(self, name, age)
        Student.__init__(self, id, room)
    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.id}")
        print(f"Room Number: {self.room_number}\n")
r1 = Resident("Hari",21,18,103)
r1.show()
r2 = Resident("dharnesh",20,78,103)
r2.show()

#8
class Restaurant:
    def __init__(self,nm,cs):
        self.restaurant_name = nm
        self.cuisine_type = cs
    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!\n")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    def display_flavors(self):
        print(f"Flavors available at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(flavor)
restaurant = Restaurant("cold summer", "classic")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
ice = IceCreamStand("fruzo", "Ice Cream")
ice.flavors = ["Vanilla", "Chocolate", "Strawberry", "watermelon"]
ice.display_flavors()

#9
class Publication:
    
    def getdata(self):
        self.title = input("Enter the title: ")
        self.price = float(input("Enter the price: "))

    def putdata(self):
        print(f"\nTitle: {self.title}")
        print(f"Price: {self.price}")

class Book(Publication):

    def getdata(self):
        super().getdata()
        self.pages = int(input("Enter the page count: "))

    def putdata(self):
        super().putdata()
        print(f"Page count: {self.pages}\n")

class Tape(Publication):
    
    def getdata(self):
        super().getdata()
        self.play_time = int(input("Enter the playing time in minutes: "))

    def putdata(self):
        super().putdata()
        print(f"Playing time: {self.play_time} minutes\n")

book = Book()
book.getdata()
book.putdata()

tape = Tape()
tape.getdata()
tape.putdata()

#10
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __gt__(self, other):
        if self.feet > other.feet:
            return True
        elif self.feet==other.feet:
            if self.inches >other.inches:
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        if self.feet < other.feet:
            return True
        elif self.feet==other.feet:
            if self.inches < other.inches:
                return True
            else:
                return False
        else:
            return False

    def __add__(self, other):
        inch = self.inches + other.inches
        feet = self.feet + other.feet
        if inch >= 12:
            feet+=1
            inch-=12
            if inch >= 12:
                feet+=1
                inch-=12
        return Distance(feet, inch)

    def display(self):
        print(f"{self.feet}'-{self.inches}\"")

feet1, inches1 = map(int, input("Enter first distance in feet and inches separated by space: ").split())
feet2, inches2 = map(int, input("Enter second distance in feet and inches separated by space: ").split())

dist1 = Distance(feet1, inches1)
dist2 = Distance(feet2, inches2)

if dist1 > dist2:
    print("First distance is greater than second distance.")
elif dist1 < dist2:
    print("First distance is less than second distance.")
else:
    print("Both distances are equal.")

dist3 = dist1 + dist2
dist3.display()

#11
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def __str__(self):
        result = ""
        for row in self.matrix:
            result += " ".join(str(x) for x in row) + "\n"
        return result

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to add.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions to subtract.")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns of first matrix must be equal to number of rows of second matrix to multiply.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result

    def __neg__(self):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[j][i] = self.matrix[i][j]
        return result

rows1, cols1 = map(int, input("Enter number of rows and columns of first matrix separated by space: ").split())
matrix1 = Matrix(rows1, cols1)
for i in range(rows1):
    matrix1.matrix[i] = list(map(int, input(f"Enter row {i+1} of first matrix separated by space: ").split()))

rows2, cols2 = map(int, input("Enter number of rows and columns of second matrix separated by space: ").split())
matrix2 = Matrix(rows2, cols2)
for i in range(rows2):
    matrix2.matrix[i] = list(map(int, input(f"Enter row {i+1} of second matrix separated by space: ").split()))

print("\nFirst matrix:")
print(matrix1)
print("Second matrix:")
print(matrix2)

result = matrix1 + matrix2
print("Sum of matrices:")
print(result)

result = matrix1 - matrix2
print("Difference of matrices:")
print(result)

result = matrix1 * matrix2
print("Product of matrices:")
print(result)

result = -matrix1
print("Transpose of first matrix:")
print(result)

result = -matrix2
print("Transpose of second matrix:")
print(result)

'''
#12
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __iadd__(self, other):
        self.seconds += other.seconds
        self.minutes += other.minutes + self.seconds // 60
        self.hours += other.hours + self.minutes // 60
        self.minutes %= 60
        self.seconds %= 60
        return self

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        if self.hours > other.hours:
            return False
        if self.minutes < other.minutes:
            return True
        if self.minutes > other.minutes:
            return False
        if self.seconds < other.seconds:
            return True
        return False

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds

    def __ge__(self, other):
        return not self < other

hours1, minutes1, seconds1 = map(int, input("Enter first time in hours, minutes, and seconds separated by space: ").split())
time1 = Time(hours1, minutes1, seconds1)

hours2, minutes2, seconds2 = map(int, input("Enter second time in hours, minutes, and seconds separated by space: ").split())
time2 = Time(hours2, minutes2, seconds2)

print("First time: ", time1)
print("Second time: ", time2)

time1 += time2
print("Sum of times: ", time1)

if time1 < time2:
    print("First time is smaller than second time.")
elif time1 > time2:
    print("First time is greater than second time.")
else:
    print("First time is equal to second time.")

if time1 >= time2:
    print("First time is greater than or equal to second time.")
else:
    print("First time is less than second time.")


