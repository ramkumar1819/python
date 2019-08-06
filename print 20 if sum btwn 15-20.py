#Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20

a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
x=a+b
if x<=20 and x>=15:
    print("20")
elif x>20:
    print("sum greater than 20")
else:
    print("sum less than 15")
