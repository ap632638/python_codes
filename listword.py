n=int(input("Enter total no. of words:"))
print("Enter ",n," words in list:")
li=[]
for i in range(n):
	li.append(input())
a=len(li[0])
b=li[0]
for i in range(1,n):
	if a<len(li[i]):
		a=len(li[i])
		b=li[i]
print("Length of longest word")
print(b,"\t length: ",a)
