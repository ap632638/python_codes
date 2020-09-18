def legend(arr):
    n = len(arr)
    legend = [arr[n-1]]    
    for i in range(n-2,-1,-1):
        flag=0
        for j in range(i+1,n):
            if(arr[i]<arr[j]):
                flag = 1
                break
        if(flag==0):
            legend.append(arr[i])
    return legend
arr = list(map(int,input("Enter Array: ").split()))
print(legend(arr))
