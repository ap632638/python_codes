n=int(input("Enter total no. of terms: "))
if n>0:
	sum = n*(n+1)/2
	print(sum)
elif n==0:
	print(0)
else:
	print("You have enterd negative number")
