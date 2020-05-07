n=int(input("Enter total no. of elements for main list:"))
print("Enter ",n," elements in list:")
lmain=[]
lsub=[]
lsm=[]
lgr=[]
lfinal=[]
for i in range(n):
	lmain.append(int(input()))
lmain.sort()
s=int(input("Enter total no. of elements for sub list:"))
print("Enter ",s," elements in sublist:")
for i in range(s):
	lsub.append(int(input()))
for i in range(n):
	if lmain[i]<lsub[1]:
		lsm.append(lmain[i])
	else:
		lgr.append(lmain[i])
for i in range(len(lsm)):
	lfinal.append(lsm[i])
for i in range(len(lgr)):
	lfinal.append(lgr[i])
print("Sorted list according to sublist:")
lmain=lfinal
print(lfinal)
	
