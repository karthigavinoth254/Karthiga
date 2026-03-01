#1)number is positive negative or zero
a=int(input("Enter the number: "))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")
#2)number is even or odd
a=int(input("Enter a number: "))
if a%2==0:
    print("Even")
else:
    print("Odd")
#3)Largest of three numbers
a,b,c=list(map(int,input("Enter three number:").split(' ')))
if(a>b and a>c):
 print("a is bigger")
elif(b>a and b>c):
 print("b is bigger")
elif(c>a and c>b):
  print("c is bigger")
else:
    print("ALL are equal")
#4)check laep year or not
year=int(input("Enter the year: "))
if year%4==0 and year%400==0 or year%100!=0:
        print("Leap year")
else:
        print("Not a leap year")
#5)eligible to vote
age=int(input("enter your age: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#6)number divisible by 5&7
a=int(input("Enter a number: "))
if a%5==0 and a%7==0:
    print("The number is divisible")
else:
    print("Not divisible")
#7)character is vowel or consonant
ch=input("enter character: ")
if ch.lower() in ['a','e','i','o','u']:
    print("Vowels")
else:
    print("Consonent")
#8)character is palindrome
text=input("Enter text:")
if text==text[::-1]:
    print("Yes,the text is palindrome")
else:
    print("No,text is not palindrome") 

#8a number is palindrome
num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome")

#9 grades based on marks if/elif(above 90-a,80-b,70-c,60-d,below 60-fail)
marks=int(input("Enter marks:"))
if marks>90:
    print("A grade")
elif marks>80:
    print("B grade")
elif marks>70:
    print("C grade")
elif marks>60:
    print("D grade")
else:
    print("Fail")
#10)Check whether a number is Armstrong number 
num = int(input("Enter a number: "))
power = len(str(num))
sum= 0
n=num
while n > 0:
    digit = n % 10
    sum=sum+digit ** power
    n //= 10
if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
#num(153)=1*3+5*3+3*3=1+125+27=153
































