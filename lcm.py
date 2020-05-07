def lcm(x,y):
	if x>y:
		min=a
	else :
		min=b
	while True:
		if (min%x==0 and min%y==0) :
			print("LCM Of ",x," and ",y," is: ",min)
			break;
		min=min+1
print("Enter any two numbers")
a=int(input("a: "))
b=int(input("b: "))
lcm(a,b)

