#list
'''a,b,c,d,e=list(map(int,input().split('#')))
print(a)
print(b)
print(c)
print(d)
print(e)

a,b,*c,d,e=list(map(float,input().split(';')))
print(a)
print(b)
print(c)
print(d)
print(e)
#slicing operator
a=["True",25,"Rudhran",12.04,5j]
c=int(input("Enter elements to access:"))
d=int(input("enter step:"))
print(a[:c:d])
#Functions
e=[1,2,3,4,5,6]
e.append(10)
print(e)
e.insert(2,11)
print(e)
e.extend([8,9,10])
print(e)
e.remove(5)
print(e)
e.pop()
print(e)
e.clear()
print(e)
del(e)
print(e)
#list comprehension
a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in a:
    if i%2==0:
        b.append(i)
    c=[i for i in a if i%2==0]
print("elements of c:",c)
print("elements of b:",b)
#list comprehension squares
nums=[1,2,3,4,5,6,7]
squares=[x*x for x in nums]
print(squares)
#list comprehension ---if else--odd/even
nums=[1,2,3,4,5,6,7]
squares=['even'if x%2==0 else 'odd' for x in nums]
print(squares)
#short hand if
a=int(input("Enter a number:" ))
print("even" if a%2==0 else "odd")'''

'''#list concatenation
a=(1,2,3,4,5)
b=(6,7,8,9,10)
print(a+b)
#Tuple
a=(1,2,3,4)
print(a[1::])
#reverse list/tuple
a=(1,2,3,4)
print(a[::-1])
#tuple concatenation
b=(1,2,3,4,5)
c=(6,7)
b=b+c
print(b)
print(type(b))
b=list(b)
print(type(b))
#index change
b[1]=100
print(b)
b=tuple(b)
print(b)
#unpacking tuple
person=("Rudhran",1.1/2,"Baby")
name,age,type=person
print(name)
print(age)
print(type)
#using astrik(*)
numbers=(1,2,3,4,5)
a,*b,c=numbers
print(a)
print(b)
print(c)
#using for with iterator
fruits=("apple","banana","cherry")
for i in fruits:
    print(i)
    if 'a' in i:
        print(i)
#by using index for in range
    for i in range(len(fruits)):
        print(i)
#by using multiplication
numbers=(12,25,4)
print(numbers*10)
#Tuple concatenation
person1=("Rudhran ")
person2=("Karthiga")
person3=("Vinoth")
result=person1+person2+person3
print(result)
#count and index 
alphabets=('A','B','C','D','E','F','A','A','A','A','A','A','A','A','A','A','A','A','A','A')
print(alphabets.count('A'))
print(alphabets.index('F'))'''
#reverse a number in single line
a=int(input()[::-1])
print(a)
#reverse a number in while loop
a=int(input())
s=0
while a:
    r=a%10
    s=(s*10)+r
    a=a//10
    print(a)






    
#accessing index value   
'''fruits=("apple", "banana", "Cherry")
for i in range(len(fruits)):
    if 'a' in fruits[i]:#a is present value
        print(fruits[i])
fruits=("apple","apple","apple","apple","banana", "Cherry")      
print(fruits.count('apple'))'''
