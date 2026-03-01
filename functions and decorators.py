'''def greet(name):
    print("Hello " +name)
greet("Vinoth")
#------------------
def greet(name):
    return("Love " +name)
x=greet("Vinoth")
print(x)
#-----------------
def multiply(a,b,c):
    return a*b*c
y=multiply(2,3,4)
print(y)
#------------------------
def sqr(x):
    return x**2
print(sqr(int(input("Enter a number: "))))
#-------------------------
#Types of arguments
#positional argument
def greet(name,gender,age):
    print("Hi i m" +name)
    print("I am" + str(age) + "years old")
    print("My gender is "+gender)
greet("Vinoth","male",32)   
#keyword argument
def greet(name,gender,age):
    print(name,age,gender)
greet(name="VINOTH",gender="male",age=32)
#default argument
def greet(name="vinoth"):
    print("hello" +name)
greet("vinoth")
#arbitary arduments
def add (*numbers):
    print(numbers)
    print(sum(numbers))
add(1,2,3,4)
#keyword arbitary arguments
def details(**data):
    print(data)
details(name="Karthiga",age=25)
#------------------------------------------
#inner function
def outer():
    def inner():
        print("Inside inner function")
    inner()
outer()
#-------------------------------------
def outer():
    def inner():
        print("Inside innner function")
    return inner
x=outer()
print(x)#print location of inner functions
x()
#-------------------------------------
#Decorator
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper
def greet():#normal funciton
    print("Hello world")
greet1=my_decorator(greet)
greet1()'''
#-----------------------------------
def my_decorator(func):
    def wrapper(name):
        print("Before execution in decorator")
        func(name)
        print("After execution in decorator")
    return wrapper
@my_decorator
def greet(name):
    print("Hello",name)
greet("Karthiga")
#---------------------------------
#Authentication decorator
def login_required(func):
    def wrapper(user):
        if user==admin:
            func(user)
        else:
            print("Access deined")
    return wrapper
def dash_board(user):
    print("welcome to dash_board",user)
dash_board("admin")
dash_board("guest")
#--------------------------------------------
'''#lambda function 1
square=lambda x:x*x
print(square(5))
#lambda function 2
x=lambda a:a**2
print(x(int(input("Enter a number:"))))
#-------------------
#lambda with map function
numbers=[1,2,3]
result=list(map(lambda x:x*2,numbers))
print(result)
#_--------------------------
#lambda with user input
add = lambda a, b: a + b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result = add(x, y)
print("add:", result)'''














































