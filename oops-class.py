'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("Rudhran", 2)
print("Enter name:", p1.name)
print("Enter age:", p1.age)
 #-----------------------------       
class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited",amount)
    def withdrawn(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("withdrawn:",amount)
        else:
            print("Insufficient balance")
    def display(self):
        print("Accountholder:",self.name)
        print("Balance:",self.balance)
acc1=BankAccount("Karthiga",1000)
acc1.deposit(2000)
acc1.withdrawn(5000)
acc1.display()
#area and circumference of the circle
class circle:
    def __init__(self,pi,r):
        self.pi=pi
        self.r=r
    def area(self):
        return self.pi*self.r*self.r
    def circumference(self):
        return 2*self.pi*self.r
c1=circle(1.54,3)
c2=circle(1.54,6)
print("Area of the circle:",c1.area())
print("Circumference of the circle:",c2.circumference())
#constructor overloading
def add (a,b):
    return a+b
def add(a,b,c):
    return a+b+c
print(add(12,5,8))
#traditional overloading
def add(a=1,b=2,c=10):
    return a+b+c
print(add(5,7))
print(add())
print(add(8,9,10))'''
#constructor overloading
class A:
    def __init__(self,x=None):
        if x is None:
            print("No argument")
        else:
            print("Argument",x)
a1=A()
a2=A(10)
#Single inheritance
class Animal:
    def speak(self):
        print("ANimal makes sound")
class Dog(Animal):
    def barks(self):
        print("Dog barks")
d=Dog()
d.speak()
d.barks()
#Multiple inheritance
class Father:
    def skill1(self):
        print("Driving")
class Mother:
    def skill2(self):
        print("cooking")
class child(Father,Mother):
    pass
c=child()
c.skill1()
c.skill2()
#multilevel inheritance
class GrandParent:
    def house(self):
        print("Grand parent house")
class Parent:
    def car(self):
        print("Parent car")
class child(Parent):
    def bike(self):
        print("child bike")
c=child()
c.car()
c.bike()
#hierarchical inheritance
class Animal:
    def speak(self):
        print("Animal makes sound")
class Dog(Animal):
    pass
class Cat(Animal):
    pass
d=Dog()
c=Cat()
d.speak()
#check MRO
class A:
    def show(self):
        print("Class A")
class B(A):
    def show(self):
        print("Class B")
class C(A):
    def show(self):
        print("Class C")
class D(B,C):
    pass
d=D()
d.show()
print(D.mro())



























