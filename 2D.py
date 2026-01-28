arr=[[12,23,32,12],[1,2,3,4,5],[2,3,4,5,5]]
k=12
for row in range(len(arr)):
    for col in range(len(arr[row])):
        if arr[row][col]==k:
            print(row,col)

