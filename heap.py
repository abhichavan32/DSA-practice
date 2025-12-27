import heapq
# numbers=[1,3,24,4,23,4,5]
# heap=[]
# for num in numbers:
#     heapq.heappush(heap,num)
# print(heap)


# arr=[2,1,2,4,5,6]
# heapq.heapify(arr)
# print(arr)

# numbers=[12,32,11,34,23,6,2]
# size=3
# heap=[]
# for num in numbers:
#     heapq.heappush(heap,num)
#     if len(heap)>size:
#         heapq.heappop(heap)
# print(heap[0])


numbers=[12,13,1,12,1,12,114,23,2]
num=[-x for x in numbers]
print(num)
heapq.heapify(num)
print ( [-x for x in num])
    