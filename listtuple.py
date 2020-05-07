n=int(input("Enter total no. of elements:"))
print("Enter ",n," elements:")
li=[]
for x in range(n):
	num=int(input())
	li.append((num,num**2))
print("The list of tuples is:")
print(li)