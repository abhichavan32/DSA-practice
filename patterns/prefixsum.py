def prefixsum (arr):
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
    return arr
arr=[12,2,3,4,12,32,3]
print(prefixsum(arr))
