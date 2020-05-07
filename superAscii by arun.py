s1=input("Enter the String: ")
a=list()
c=0
k=0
for i in range(0,26):
	a.append(0)
for i in range(0,len(s1)):
	k=int(ord(s1[i]))-97
	a[k]+=1
for i in range(0,26):
	if(a[i]==i+1 or a[i]==0):
		c=1	
	else:
		c=0
		break
if(c!=0):
	print(s1+" is a Super Ascii String")
else:
	print(s1+" is not a Super Ascii String")



def remdup(l):
	new_l=[]
	new_l.append(l[0])
	for x in range(1,len(l)):
		count=0
		for y in range(0,len(new_l)):
			if(l[x]==new_l[y]):
				count+=1
				break
		if(count==0):
			new_l.append(l[x])
	return new_l




def transpose(m):
	transpose_list=[]
	for x in range(0,len(m[0])):
		l=[]
		for y in range(0,len(m)):
			l.append(m[y][x])
		transpose_list.append(l)
	return transpose_list




	