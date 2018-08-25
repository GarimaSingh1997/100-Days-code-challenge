m=int(input("Enter a number "))
n=int(input("Enter second number "))
if(m>n):
    min1=m
else:
    min1=n
while(1):
    if(min1%m==0 and min1%n==0):
        print("LCM is: ",min1)
        break
    min1=min1+1
