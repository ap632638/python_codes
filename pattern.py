for x in range(5):
    for y in range(x+1):
        print("*",end=" ")
    print()
for x in range(6):
    for y in range(6-x):
        print("*",end=" ")
    print()
d = 10
for x in range(d):
    for y in range(d):
        if(x+y>=d):
            print("1",end=" ")
        else:
            print(" ",end="")
    print()

for x in range(d):
    for y in range(d):
        if(y>=x):
            print("1",end=" ")
        else:
            print(" ",end="")
    print()