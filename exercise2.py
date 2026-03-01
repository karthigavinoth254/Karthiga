'''#which is greater
a,b,c=list(map(int,input("Enter three number:").split(' ')))
if(a>b and a>c):
 print("a is bigger")
elif(b>a and b>c):
 print("b is bigger")
elif(c>a and c>b):
  print("c is bigger")
else:
 print("All are equal")
#nested if
a=(int(input("Enter a number:")))
if a>0:
       if(a%2==0):
         print("Even postive")
       else:
           print("Odd positive")

else:
     if(a%2==0):
         print("Even negative")
     else:
                  print("Odd negative")

    
#match case single 
day=int(input("Enter the number of days:"))
match day:
              case 1:
                     print("Monday")
              case 2:
                     print("Tuesday")
              case 3:
                     print("Invalid Input")
#match case multiple 
day=int(input("Enter the number of days:").strip())
match day:
              case'm'|'t'|'w'|'th'|'f':
                    print("Week days")
              case's'|'su':
                        print("Week end")
              case _:
                         print("Invalid Input")'''

#match case practice
signal=input("color of signal:").strip()
match signal:
    case'red':
        print("Stop")
    case'yellow':
        print("Get ready")
    case'green':
        print("Go")
    case _:
        print("Invalid Input")




                         
'''#prime or not
a=int(input("Enter the number: "))
c=0
for i in range(2,a):
            if a%i==0:
              c+=1
            if c==0:
                   print("Prime")
            else:
                    print("not a prime")

#shorthand if
a=int(input())
print("even" if a%2==0 else "odd")

#list comprehension
a=[1,2,3,4,5]
b=[]
for i in a:
    if i%2==0:
        b.append(i)
        c=[i for i in a if i%2==0]
        print(a)
        print(b)
        print(c)'''

#reverse a number
a=int(input())
s=0
while a:
    r=a%10
    s=(s*10)+r
    a=a//10
    print(S)
            



        
