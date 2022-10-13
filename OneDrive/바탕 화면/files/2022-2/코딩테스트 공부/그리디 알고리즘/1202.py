import sys
import heapq
from wsgiref.handlers import BaseCGIHandler

N,K = map(int,sys.stdin.readline().split())

jew = []
bag = []

for _ in range(N):
    weight, price = map(int,sys.stdin.readline().split())
    heapq.heappush(jew,[weight,price])

for _ in range(K):
    capacity = int(sys.stdin.readline())
    bag.append(capacity)

bag.sort()

heap = []
total = 0

for i in bag:
    while(jew and i >= jew[0][0]):
        pop_value = heapq.heappop(jew)
        heapq.heappush(heap,-pop_value[1])
    
    if(heap):
        total -= heapq.heappop(heap)
    
print(total)