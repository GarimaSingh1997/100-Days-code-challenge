n=int(input("Enter a number who you find the smallest divisor "))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("Smallest divisor is ",a[0])
