from heapq import *

N = int(input())

heap = []

for i in range(N):
    card = int(input())
    heappush(heap,card)

if(N == 1):
    print(0)
    exit()

total = 0

while(True):
    sum = 0
    sum += heappop(heap)
    sum += heappop(heap)
    total += sum
    if(len(heap) == 0):
        break
    heappush(heap,sum)

print(total)