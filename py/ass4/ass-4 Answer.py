#1
x=lambda x,y:x*y
print(x(5,3))

#2
l=[1,2,3,4,5,6,7,8,9,0]
y=filter(lambda a:a%2!=0,l)
print(list(y))

#3
eve_list=[i for i in range(1,101,1) if i%2==0]
for i in eve_list:
    print(i)

#4
mylist = [1452, 11.23, 1+2j, True, 'Welcome', (0, -1), [5, 12], {"class":'IT', "semester":'IV'}]
a=map(lambda x:(x,type(x)),mylist)
for i,j in a:
    print(f'item:{i} ,datatype:{j}')
    
#5.1
my_str="welcome to my class!"
upper_str="".join(map(str,map(lambda x:x.upper(), my_str)))
print(upper_str)

#5.2
my_list=[2,3,4,5,6,7,8,9]
m_list=list(map(lambda x:x*10,my_list))
print(m_list)

#5.3
my_tuple=('php','java','python','c++','c')
tittle=tuple(map(lambda x:x.title(),my_tuple))
print(tittle)

#5.4
my_set={2,3,4,5,6,7,8,9}
cube=set(map(lambda a:a**3,my_set))
cube_set=sorted(cube)
print(cube_set)

#5.5
my_list=['a','b','b','d','e']
my_tuple=('PHP','Java','Python','C++','C')
joined_list=list(map(lambda a,b:a+'_'+b,my_list,my_tuple))
print(joined_list)

#6
my_list=[2,3,4,5,6,7,8,9]
cube=[]
for i in my_list:
    if i%2==0:
        cube.append(pow(i,3))
print (cube)

#7
name="   GUNA  SEKAR   "
print("name :",name,"\nlstrip :",name.lstrip(),'\nrstrip :',name.rstrip(),'\nstrip :',name.strip())

#8
circle=(1.23456,2.34567,3.45678,4.56789,5.67890)
rounded_area=tuple(round(area,dec)for dec,area in enumerate(circle,start=1))
print(rounded_area)

#9
l1=[1,2,3,4,5]
l2=[5,6,7,8,9]
def common(a,b):
    if(x in b for x in a):
        return("True")
    else:
        return("false")
print(common(l1,l2))

#10
n = int(input("enter the no of rows :"))
for i in range(n):
 
    print(' '*(n-i),end="")
 
    print(' '.join(map(str, str((11**i)))))


#11
def string_length(string):
    return len(string)

def string_reverse(string):
    return string[::-1]

def string_concatenation(s1, s2):
    return s1 + s2

def string_comparison(s1, s2):
    if s1 == s2:
        return "The strings are equal."
    else:
        return "The strings are not equal."
while(True):
    print("\nMenu:")
    print("1. String length")
    print("2. String reverse")
    print("3. String concatenation")
    print("4. String comparison")
    print("5. exit")
    
    ch=input("Enter your choice : ")
    
    if ch=="1":
        st=input("Enter string to find length : ")
        print("String length:", string_length(st))
        
    elif ch=="2":
        s1 =input("Enter string to reverse : ")
        print("Reversed string:", string_reverse(s1))
        
    elif ch=="3":
        string1=input("Enter first string: ")
        string2=input("Enter second string: ")
        print("Concatenated string:", string_concatenation(string1, string2))
        
    elif ch=="4":
        string1=input("Enter first string: ")
        string2=input("Enter second string: ")
        print("Comparison:", string_comparison(string1, string2))
        
    elif ch=='5':
        print('you are on exit')
        break
        
    else:
        print("Invalid choice.")
    
#12
def fun(a,b,c=5):
    print(a,b,c)
fun(1,c=3,b=2)

#13
def func(a,b=4,c=5):
    print(a,b,c)
func(1,2)

#14
def fun(a,b,c=5):
    print(a,b,c)
fun(1,c=3, b=2)

#15
def fun(a,*pargs):
    print(a,pargs)
fun(1,2,3)

#16
def fun(a,**kargs):
    print(a,kargs)
fun(a=1,b=2,c=3)

#17
def fun(a,b,c=3,d=4):
    print(a,b,c,d)
fun(1,*(5,6))

#18
def triangle(rows):
    for i in range(1,rows+1):
        print(" "*(rows-i)+'* '*(i))
triangle(6)

def inverted_triangle(rows):
    for i in range(rows,0,-1):
        print(" "*(rows-i)+'* '*(i))
inverted_triangle(5)

def left_triangle(rows):
    for i in range(1,rows+1):
        print("* "*i)
left_triangle(5)

def right_inv_tri(rows):
    for i in range(rows, 0, -1):
        for x in range(rows-i,0,-1):
            print(" ",end=" ")
        for j in range(1, i+1):
            print('*', end=" ")
        print()
    print()
right_inv_tri(7)

#19
def left_num_tri(rows):
    for i in range(1,rows+1):
        for j in range(1,i+1):
             print(j,end=" ")
        print()
    print()
left_num_tri(5)

def num_tri(rows):
    k = 0
    count=0
    count1=0
    for i in range(1,rows+1):
        for j in range(1, (rows-i)+1):
            print("  ", end="")
            count+=1
            
        while k!=((2*i)-1):
            if count<=rows-1:
                print(i+k, end=" ")
                count+=1
            else:
                count1+=1
                print(i+k-(2*count1), end=" ")
            k += 1
    
        count1 = count = k = 0
        print()
    print()
num_tri(5)

def right_inv_num_tri(rows):
    for i in range(rows, 0, -1):
        for x in range(rows-i,0,-1):
            print(" ",end=" ")
        for j in range(1, i+1):
            print(j, end=" ")
            
        print()
    print()
right_inv_num_tri(5)

def inv_tri(rows):
    k = 0
    count=0
    count1=0
    
    for i in range(rows,0,-1):
        for j in range(1, (rows-i)+1):
            print("  ", end="")
            count+=1
            
        while k!=((2*i)-1):
            if count<=rows-1:
                print(i+k, end=" ")
                count+=1
            else:
                count1+=1
                print(i+k-(2*count1), end=" ")
            k += 1
    
        count1 = count = k = 0
        print()
inv_tri(5)

#20
def hms_to_secs(h=0, m=0, s=0):
    return h * 3600 + m* 60 + s

total_seconds = hms_to_secs(1,30,30)
print(f"{total_seconds} seconds")
total_seconds = hms_to_secs(1,*(30,30))
print(f"{total_seconds} seconds")
total_seconds = hms_to_secs(s=30,h=1,m=30)
print(f"{total_seconds} seconds")
total_seconds = hms_to_secs()
print(f"{total_seconds} seconds")
total_seconds = hms_to_secs(1,**{'m':30,'s':30})
print(f"{total_seconds} seconds")

#21
def make_shirt(s,m):
    print(f"the shirt size is {s} and message is '{m}'")
    
make_shirt(40,'gunasekaran')
make_shirt(m='gunasekaran',s=40)

#22
def fav_book(title):
    if title.lower() =='ponniyin selvan':
        print(f'one of my favourate book is {title}')
    else:
        print(f"I've read that book {title}")
fav_book('Ponniyin Selvan')
fav_book("Ocean")
fav_book('Gardian of the Galaxy')

#23
current_users = ['kavi', 'arun', 'john', 'kevin', 'sara']
new_users = ['Sam', 'JaCkSon', 'Kavi', 'Raj', 'Emilia']

user=[x.lower() for x in current_users]
n_user=[x.lower() for x in new_users]

for new_use in n_user:
    if new_use in user:
        print(f"Sorry, {new_use} is already taken. Please choose a new username.")
    else:
        print(f"{new_use} is available!")

#24
import string,random
def pass_gen():
    n=random.randint(8,12)
    ch=string.ascii_letters+string.digits+string.punctuation
    pas=[]
    for i in range(n):
        chr=random.choice(ch)
        while any(c==chr for c in pas):
            chr=random.choice(ch)
        pas.append(chr)
    return ''.join(pas)
            
print(pass_gen())


