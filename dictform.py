n=int(input("Enter upper range: "))
d={}
for i in range(1,n+1):
	d.update({i:i**2})
print("Dictionary generated is: ")
print(d)