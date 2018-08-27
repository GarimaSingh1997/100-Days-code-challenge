N = int(input("Enter a number "))
if(N%2==0):
    if(N<6 or N>20):
        print("Not weird")
    else:
        print("Weird")
else:
    print("Weird")
