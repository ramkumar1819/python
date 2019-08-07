#Python function that takes a sequence of numbers and determines if all the numbers are different from each other
def difflist(list1):
    if(len(list1)==(len(set(list1)))):
        return("all element in list are different")
    else:
        return("element in list have duplicate")
print(difflist([1,2,3,4,4]))
print(difflist([1,2,3]))
