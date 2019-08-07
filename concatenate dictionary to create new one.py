##Python program to concatenate following dictionaries to create a new one
dic1={"name":"ram"}
dic2={"age":19}
dic3={}
for x in(dic1,dic2):
    dic3.update(x)
print(dic3)
