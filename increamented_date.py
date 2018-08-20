date=input("Enter date/month/year : ")
dd,mm,yy=date.split('/')
dd=int(dd)
mm=int(mm)
yy=int(yy)
if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max=31
elif(mm==4 or mm==6 or mm==9 or mm==11):
    max=30
elif(mm%4==0 or mm%100==0 and mm%400==0):
    max=29
else:
    max=28
if(mm<1 or mm>12):
    print("Date is invalid")
elif(dd<1 or dd>max):
    print("Date is invalid")
elif(dd==max and mm!=12):
    dd=1
    mm=mm+1
    print("Enter the increamental date : ",dd,mm,yy)
else:
    dd=dd+1
    print ("The increamental date is ",dd,mm,yy)
