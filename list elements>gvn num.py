list1=[3,4,5]
n=int(input("enter the number"))
if (all(x>n for x in list1)):
    print("all value in list greater than given number")
else:
    print("all value in list lesser than given number")
