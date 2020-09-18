def arrayReversal(arr,start,end):
    s= start
    e = end
    while(start<end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start+=1
        end-=1
    return arr
def arrayRotation(arr,nor):
    n = len(arr)
    rr = nor%n
    if(rr==0):
        return arr
    else:
        arr = arrayReversal(arr,0,rr-1)
        arr = arrayReversal(arr,rr,n-1)
        arr = arrayReversal(arr,0,n-1)
    return arr
arr = [1,2,3,4,5]
print(arrayRotation(arr,40))
