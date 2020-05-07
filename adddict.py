n=int(input("Enter total key value pair you want to add: "))
d={}
for i in range(n):
	key=int(input("Enter key(integer) to add: "))
	value=input("Enter value to add for the key: ")
	d.update({key:value})
print("Updated dictionary is:")
print(d)