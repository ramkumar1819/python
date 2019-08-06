#Python program to test whether a passed letter is a vowel or not

str1=str(input("enter the letter"))
vowel=['a','e','i','o','u']
if str1 in vowel:
    print("%c is vowel"%str1)
else:
    print("%c is not a vowel"%str1) 
