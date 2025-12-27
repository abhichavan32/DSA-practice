arr=[1,3,2,4,5,6]
n=len(arr)
for i in range(n-1):
    small=i
    for j in range(i+1,n):
        if arr[j]<arr[small]:
            small=j
    arr[i],arr[small]=arr[small],arr[i]
print(arr)