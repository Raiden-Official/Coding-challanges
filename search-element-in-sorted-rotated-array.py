def searchKey(a, start, end, key):
    mid = int((start + end)/2)

    if(a[mid] == key):
        print("Key found at:",mid+1)
        return mid
    
    if(start > end):
        print("key not found")
        return -1
    if(a[start] <= a[mid]):
        if(key >= a[start] and key <= a[mid]):
            return searchKey(a, start, mid-1, key)
        else:
            return searchKey(a, mid+1, end, key)
    
    else:
        if(a[mid+1] <= a[end] and key > a[mid+1] and key <= a[end]):
            return searchKey(a, mid+1, end, key)
        else:
            return searchKey(a, start, mid-1, key)        
# Test-cases:
a = [1,2,3,4,5,6,7,8,9] # key = 9
b = [6,7,8,9,1,2,3,4,5] # key = 7
c = [4,5,6,7,8,9,1,2,3] # key = 9
d = [7,8,9,1,2,3,4,5,6] # key = 9

# Checking the test cases:
searchKey(a, 0, len(a)-1, 9)
searchKey(b, 0, len(b)-1, 7)
searchKey(c, 0, len(c)-1, 9)
searchKey(d, 0, len(d)-1, 10)
