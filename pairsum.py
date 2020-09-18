def pairsum(arr,num):
    arr.sort()
    n= len(arr)
    i,j,pair = 0,n-1,0
    while(i<j):
        summ = arr[i] + arr[j]
        if(summ<num):
            i+=1
        elif(summ>num):
            j-=1
        else:
            pair+=1
            i+=1
            j-=1
    return pair
arr = list(map(int,input("Enter Array: ").split()))
num = int(input("Enter Num "))
print(pairsum(arr,num))
