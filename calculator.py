def add(x,y):
	print("Addition of ",a," and ",b," is: "+str(a+b))
def sub(x,y):
	print("Subtraction of ",a," and ",b," is: "+str(a-b))
def mul(x,y):
	print("Multiplication of ",a," and ",b," is: "+str(a*b))
def div(x,y):
	print("Division of ",a," and ",b," is: "+str(a/b))
while True:
	print("Choose from the below option:")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("5. Exit")
	ch=int(input("Enter your choice: "))
	if ch==1:
		print("Enter two numbers")
		a=int(input("a: "))
		b=int(input("b: "))
		add(a,b)
	elif ch==2:
		print("Enter two numbers")
		a=int(input("a: "))
		b=int(input("b: "))
		sub(a,b)
	elif ch==3:
		print("Enter two numbers")
		a=int(input("a: "))
		b=int(input("b: "))
		mul(a,b)
	elif ch==4:
		print("Enter two numbers")
		a=int(input("a: "))
		b=int(input("b: "))
		div(a,b)
	elif ch==5:
		exit()
	else:
		print("Invalid Choice")
