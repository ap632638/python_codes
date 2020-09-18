def maxSubArray(arr):
    max_so_far = -1000000000000000000
    ending_here = 0
    for i in range(len(arr)):
        ending_here = ending_here + arr[i]
        if(ending_here<0):
            ending_here = 0
        if(max_so_far<ending_here):
            max_so_far = ending_here
    return max_so_far
arr = list(map(int,input("Enter array: ").split()))
print(maxSubArray(arr))
