print("Enter marks obtained by student:-")
mt=int(input("Mathematics: "))
sc=int(input("Science: "))
ss=int(input("Social Studies: "))
en=int(input("English: "))
hi=int(input("Hindi: "))
total=mt+sc+ss+en+hi
per=total/5
print("Total= "+str(total))
print("Percentage= "+str(per))
if(per>=75):
	print("First Divison")
if(per<75 and per>=55):
	print("Second Divison")
if(per<55 and per>=33):
	print("Third Divison")
if(per<33):
	print("Fail")