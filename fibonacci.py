n=int(input("Enter no. of terms you want: "))
t1=0
t2=1
s=0
for x in range(1,n+1):
	print(t1)
	s=t1+t2
	t1=t2
	t2=s

