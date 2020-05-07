n=int(input("Enter total number of elements of first dictionary: "))
d1={}
for i in range(n):
	key=int(input("Enter key(int) : "))
	value=input("Enter value for key: ")
	d1.update({key:value})
t=int(input("Enter total number of elements of second dictionary: "))
d2={}
for i in range(t):
	key=int(input("Enter key(int) : "))
	value=input("Enter value for key: ")
	d2.update({key:value})
d1.update(d2)
print("dictionary after concatenation:")
print(d1)