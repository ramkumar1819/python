#Python program to convert a tuple to a dictionary
tup=((2,'r'),(1,'a'))
print(dict((x,y) for y,x in tup))
