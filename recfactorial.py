def fact(a):
	if(a>1):
		return a*fact(a-1)
	if a==1:
		return 1
n=int(input("Enter any positive integer: "))
print("Factorial of ",n," is: ",fact(n))