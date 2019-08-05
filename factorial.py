n=int(input("enter the number"))
m=n
fact=1
if(n==0):
    print("factorial is 1")
elif (n>1):
    while (n>1):
         fact=fact*n
         n-=1
    print("factorial of %d is %d"%(m,fact))
elif (n==1):
    print("factorial is 1")
else:
    print("factorial doesn't exist")
