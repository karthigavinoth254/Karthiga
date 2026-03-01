#print statements
'''print("My world Vinoth")
print("My son Rudhran")
print("Hello world",end='*')
print("Rudhran")
print("My son Rudhran","Active","Energy",sep='$')
print("My son Rudhran","Active","Energy")
#comments
#print("dgcdjcn")
print("hcjhid")
print("xfsuytdusbc")
print("fgejfk")
#variables type identification
a=234
b7=78.98
c=d=e="10.45"
print(type(a))
a=234
b7=78.98
c=d=e="10.45"
print(type(c))
#modulus
X=5
Y=2
print(X%Y)
#floor division
X=5
Y=2
print(X//Y)
#division
X=5
Y=2
print(X/Y)
#exponent
#5 power 2
X=5
Y=2
print(X**Y)
#2 power 5
x=5
y=2
print(y**x)
#Variables
#assign value to variables
x="car"
y="bike"
print(x)
print(y)
#multiple values and variables
x,y,z=("car","bike","cycle")
print(x,y,z)
#multiple variables to single value
x=y=z="Apple"
print(x)
print(y)
print(z)
#single variable multiple value
vehicles=["Car","Bike","Cycle"]
x,y,z=vehicles
print(x)
print(y)
print(z)
#output variables
x=4
y="Karthiga"
print(x,y)
#string concatenation
x="Karthiga"
y="Vinoth"
print(x+y)
#string concatenation with space
x="Karthiga "
y="Vinoth"
print(x+y)
#data types
x=str(3)
y=float(4)
z=int(6)
print(x)
print(y)
print(z)
x="Karthiga" #string
print(x)
print(type(x))
x=25 #integer
print(type(x))
x=25.5 #float
print(type(x))

x=["Car,Bike,Cycle"]
print(x)
print(type(x))#list
x=("Car","Bike","Cycle")
print(x)
print(type(x))#tuple
x=range(20)
print(x)
print(list(x))#(0,1,2,3,4,5,6,7,8,9)
x={"Name":"Vinoth","age":32}
print(x)
print(type(x))#dictionary
x={"Car","Bike","Cycle"}
print(x)
print(type(x))#set
x=frozenset({"car","bike","Cycle"})
print(x)
print(type(x))#frozenset
x="True"
print(x)#bool
#operators
#Arithmetic operators
x=12
y=25
print(x+y)#37
print(x-y)#-13
print(x*y)#300
print(x/y)#0.48
print(x%y)#0
print(x**y)#953962166440690129601298432
print(x//y)#2

#comparison operator
x=5
y=10
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#Logical operator
x=5
print(x)
print(x>3 and x<10)
print(x<5 or x<10)
print(not(x>3 and x<10))

maths=45
chem=100
print(maths>50 and chem>50)#and operator (multiplication)
print(not(maths>50 and chem>50))#not operator  inverse
print(maths>50 or chem>50)#or opeartor (addition)
#Bitwise operator

print(10&35)#2
print(10|35)#43
print(10^35)#92
print(~35)
print(~10)

a=int(input('Enter a number'))
print(type(a))
print(int(90.7))
print(type(a))

a=input().split('#')
print(a)
a=input().split('%')
print(a)



#leap year
a=int(input("enter the year:"))
if ((a%400==0)or(a%100!=0 and a%4==0)):
    print("leap year")
else:
    print("not a leap year")

                



