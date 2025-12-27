arr=[1,3,2,4,6,5]
n=len(arr)
for i in range(1,n):
    curr=arr[i]
    prev=i-1
    while (prev >= 0 and arr[prev]>curr):
        arr[prev+1]=arr[prev]
        prev -= 1
    arr[prev+1]=curr
print(arr)
