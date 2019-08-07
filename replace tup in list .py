#Python program to replace last value of tuples in a list

list1=[(10,20,30),(40,50,60),(70,80,90)]
print([x[:-1]+(100,) for x in list1])
