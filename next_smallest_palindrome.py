def splitnum(n):
    n = str(n)
    size = len(n)
    mid = size//2
    if(size%2==0):
        return (n[:mid],'',n[mid:])
    else:
        return (n[:mid],n[mid],n[mid+1:])
def next_small_palindrome(n):
    size = len(str(n))
    if(n<9):
        return n + 1
    if(n<10):
        return 11
    left,mid,right = splitnum(n)
    if(n == (10**size)-1):
        return 10**size + 1
    elif(mid == ''):
        if(not int(left[::-1])>int(right)):
            left = str(int(left) + 1)
        right = left[::-1]
    else:
        if(not int(left[::-1])>int(right)):
            left = str(int(left + mid)+1)
        mid = left[-1]
        left = left[:-1]
        right = left[::-1]
    return int(left + mid + right)
print(next_small_palindrome(94187978322354844544))
