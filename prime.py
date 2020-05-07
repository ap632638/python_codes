n=int(input("Enter a number: "))
for i in range(2,n//2):
	if n%i==0:
		flag=0
		break
	else:
		flag=1
if flag==0:
	print(n," is not a prime number")
else:
	print(n," is a prime number")