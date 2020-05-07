n=int(input("Enter any number: "))
s=0
i=n
m=n
arm=0
while i>0:
	s=s+1
	i=i//10
while m>0:
	p=m%10
	arm=arm+p**s
	m=m//10
if arm==n:
	print(n," is a armstrong number")
else:
	print(n," is not a armstrong number")