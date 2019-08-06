# Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged

str1=str(input("enter the string"))
a=str1[0:1]
str2="Is"
if a==str2:
    print(str1)
else:
    print("Is"+str1)
