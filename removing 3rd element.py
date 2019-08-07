#Python program to remove and print every third number from a list of numbers until the list becomes empty
list1=[1,2,3,4,5,6,7]
idx=0
count=3-1
x=len(list1)
while x>0:
    idx=(idx+count)%x
    print(list1.pop(idx))
    x-=1


