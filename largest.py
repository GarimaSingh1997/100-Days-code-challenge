a=float(input("Enter a first number"))
b=float(input("Enter a second number"))
c=float(input("Enter a third number"))
if(a>b and a>c):
    print(a, " is largest")
elif (b>c and b>a):
    print(b, " is largest")
else:
    print(c, " is largest")
