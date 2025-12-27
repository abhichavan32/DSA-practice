arr=[12,14,16,18,19,21,24,26,28]

end=len(arr)-1
s=0

search=28

for i in range (len(arr)):
    mid= (s+end)//2
    if arr[mid]==search:
        print("search element found")
        break
    elif search > arr[mid]:
        s=mid+1
    else:
        end=mid-1
else:
    print("element not found")



