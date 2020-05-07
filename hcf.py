def hcf(x,y):
	if x<y:
		sm=x
	else:
		sm=y
	for i in range(1,sm+1):
		if (x%i==0 and y%i==0):
			h=i
	return h
print("Enter two numbers:-")
a=int(input("a: "))
b=int(input("b: "))
print("HCF of ",a," and ",b," is: ",hcf(a,b))
