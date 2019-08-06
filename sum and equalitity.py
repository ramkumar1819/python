#Python program to calculate the sum of three given numbers, if the values areequal then return thrice of their sum

a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
c=int(input("enter the 3rd number"))
x=a+b+c
print("sum of %d %d %d is %d"%(a,b,c,x))
if a==b==c:
    print(3*(x))
else:
    print("three numbers are different")
