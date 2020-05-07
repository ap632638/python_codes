n=int(input("Enter total key value pair you want to add: "))
d={}
for i in range(n):
	key=int(input("Enter key(integer) to add: "))
	value=input("Enter value to add for the key: ")
	d.update({key:value})
k=int(input("Enter the key to search: "))
if k in d.keys():
	print("Key ",k," is present and value is: ",d[k])
else:
	print("key ",k," is not found")

