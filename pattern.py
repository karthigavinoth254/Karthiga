
'''#pattern printing
#matrix
a=int(input())
for i in range (a):
    for j in range (a):
        print(i,j, end=' ',sep='')
    print()
 #diagonal       
a=int(input())
for i in range (a):
    for j in range (a):
        if i==j:
            print('*', end=' ',sep='')
        else:
            print(' ',end=' ',sep='')
    print()
#cross diagonal
a=int(input("No of rows: "))
for i in range (a):
    for j in range (a):
        if i==j or j==a-1-i:
            print('*', end=' ',sep='')
        else:
            print(' ',end=' ',sep='')
    print()'''      
'''#Right angled triangle
r=int(input("enter the no of rows:")) 
for i in range(1, r+ 1):
    for j in range(1,r+1):
        if j==1 or i==r or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#3 rows star
a=int(input())
for i in range(1,a+1):
    for j in range(1,a-1):
         print("*", end=" ")
    else:
        print(" ", end=" ")
    print()
#left angled
r = int(input("Enter number of rows: "))

for i in range(1, r + 1):
    for j in range(1, r + 1):
        if j <= r - i:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
#all row star
r=int(input("Enter the rows: "))
for i in range(1, r+1):
    for j in range(1, r-1):
        print("*", end=" ")
    print()     
#Daimond pattern
r=int(input("Enter the rows: "))#get input
for i in range(1,r+1):#loop runs 1 to 7(upper pramid)uu
    for space in range(r-i):#(loop print space b/w * to center ---space decrease when i increase)
        print(" ",end="")
    for star in range(2*i-1):#(loop print * no: of * in each row is  2 * i - 1----(*) increase when i increase)
        print("*",end="")
    print()
for i in range(r-1,0,-1):#(loop print -2 to 1 row in lower pramid)
    for space in range(r-i):#(loop print space b/w * to center ---space decrease when i decrease)
        print(" ",end="")
    for star in range(2*i-1):#(loop print * no: of * in each row is  2 * i (*) decrease when i decrease)
        print("*",end="")
    print() ''' 













    
   
