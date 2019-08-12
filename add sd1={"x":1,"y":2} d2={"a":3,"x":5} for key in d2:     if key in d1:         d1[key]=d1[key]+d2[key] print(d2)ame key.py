#Python program to combine two dictionary adding values for common keys
d1={"x":1,"y":2}
d2={"a":3,"x":5}
for key in d2:
    if key in d1:
        d1[key]=d1[key]+d2[key]
print(d1)
