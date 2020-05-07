n=int(input("Enter a number: "))
if n>1:
	i=1
	fact=1
	while i<=n:
		fact=fact*i
		i+=1
	print(fact)
elif n==0:
	print(1)
else:
	print("Negative number factorial not possible")
