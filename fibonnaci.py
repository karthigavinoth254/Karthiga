'''#fibonnaci series
a=int(input())
b,c=0,1
if a==1:
      print(b)
elif a==2:
    print(b,c)
elif(a>2):
    for i in range(a-2):
        d=b+c
        b,c=c,d
        print(d)'''
#fibonnaci series with function
y=10
def fibo(a):
    b, c = 0, 1
    if a == 1:
        print(b)
        return b
    elif a == 2:
        print(b, c)
        return c
    elif a > 2:
        print(b, c, end=" ")
        for i in range(a - 2):
            d = b + c
            b, c = c, d
            print(d, end=" ")
        return d
a=int(input())
b=fibo(a)
print(b)
