#get the ASCII value of a character

print(ord('a'))
print(ord('@'))
print(ord('1'))
