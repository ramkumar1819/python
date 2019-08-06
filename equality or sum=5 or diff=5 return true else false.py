# Python program that will return true if the two given integer values are equal or their sum or difference is 5


a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
if a==b:
    print("true")
elif a+b==5:
    print("true")
elif (abs(a-b)==5):
    print("true")
else:
    print("false")
