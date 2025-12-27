def insertion_sort(arr):
    n=len(arr)
    for i in range(1, n):
        temp=arr[i]
        j=i-1
        for j in range(i-1, -1, -1):
            if arr[j] > temp:
                arr[j+1] = arr[j]
            else:
                break
        arr[j+1] = temp
    return arr  
print(insertion_sort([64, 34, 25, 12, 22, 11, 90]))