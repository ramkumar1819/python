n=int(input("enter the year"))
if(n%400==0):
    print("%d is leap year"%n)
elif(n%100==0):
    print("%d is not a leap year"%n)
elif(n%4==0):
    print("%d is a leap year"%n)
else:
    print("%d is not a leap year"%n)
