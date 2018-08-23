n=int(input("Enter the number of elements to be inserted"))
b=[]
for i in range(0,n):
    a=int(input("Enter elements: "))
    b.append(a)
sum1=0
sum2=0
sum3=0
for j in b:
    if (j>0):
        if(j%2==0):
            sum1=sum1+j
        else:
            sum2=sum2+j
    else:
        sum3=sum3+j
print("Sum of all positive even number = ",sum1)
print("Sum of all positive odd number = ",sum2)
print("Sum of all negative number = ",sum3)
    
    
