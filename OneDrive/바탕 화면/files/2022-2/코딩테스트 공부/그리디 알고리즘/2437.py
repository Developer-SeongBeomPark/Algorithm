import sys
import heapq
from itertools import combinations

N = int(sys.stdin.readline())

weights = list(map(int,sys.stdin.readline().split()))

arr = []

for i in range(1,N+1):
    a = list(combinations(weights,i))
    for j in range(len(a)):
        heapq.heappush(arr,sum(a[j]))

arr = list(set(arr))
heapq.heapify(arr)

value = 1

while True:
    min_value = heapq.heappop(arr)
    if(value != min_value):
        break
    value += 1

print(value)

