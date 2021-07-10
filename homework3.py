#2
word=input("Please input a word to reverse:")
for i in range(len(word) -1, -1, -1):
    print(word[i], end="")
print("\n")




#3
height=int(input("Enter triangle height:"))
for i in range(height):
    for h in range(i):
        print('*', end="")
    print('')
for i in range(height, 0, -1):
    for h in range(i):
        print('*', end="")
    print('')




#4
a=int(input("Enter A"))
b=int(input("Enter B"))
if a<b:
    for i in range(a, b +1):
       print(i, end=" ")
else:
   for i in range(a, b -1, -1):
       print(i, end=" ")
print("\n")




#5
a=int(input("Enter A"))
b=int(input("Enter B"))
if a<b:
    for i in range(a, b +1):
       print(i, end=" ")
else:
    print("Wrong values")

