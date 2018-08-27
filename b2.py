lst = []
num = int(input("Enter size of list: \t"))
for n in range(num):
 numbers = int(input("Enter any number: \t"))
 lst.append(numbers)
 
x = int(input("\nEnter number to search: \t"))
 
flag=0
 
for i in range(len(lst)):
 if lst[i] == x:
     flag=1
     print("\n%d found at position %d" % (x, i))
     break
if not flag:
 print("\n%d is not in list" % x)
