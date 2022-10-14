import sys
import heapq

zero_list = []
plus_list = []
minus_list = []

N = int(sys.stdin.readline())

for _ in range(N):
    value = int(sys.stdin.readline())
    if(value == 0):
        zero_list.append(value)
    elif(value < 0):
        heapq.heappush(minus_list, value)
    else:
        heapq.heappush(plus_list, -value)



plus_total = 0
minus_total = 0

if(zero_list):
    heapq.heappush(minus_list, 0)
    if(len(minus_list) == 1):
        minus_total = 0
    else:
        if(len(minus_list) % 2 == 0):
            while minus_list:
                minus_total += heapq.heappop(minus_list) * heapq.heappop(minus_list)
        else:
            while len(minus_list) > 1:
                minus_total += heapq.heappop(minus_list) * heapq.heappop(minus_list)
else:
    if(len(minus_list) % 2 == 0):
        while minus_list:
            minus_total += heapq.heappop(minus_list) * heapq.heappop(minus_list)
    else:
        while len(minus_list) > 1:
            minus_total += heapq.heappop(minus_list) * heapq.heappop(minus_list)
        minus_total += heapq.heappop(minus_list)

if(len(plus_list) > 0):
    if(len(plus_list) % 2 == 0):
        while plus_list:
            x = heapq.heappop(plus_list)
            y = heapq.heappop(plus_list)
            if(x == -1 or y == -1):
                plus_total -= x
                plus_total -= y
            else:
                plus_total += x * y
    else:
        while len(plus_list) > 1:
            x = heapq.heappop(plus_list)
            y = heapq.heappop(plus_list)
            if(x == -1 or y == -1):
                plus_total -= x
                plus_total -= y
            else:
                plus_total += x * y
        plus_total -= heapq.heappop(plus_list)

print(plus_total + minus_total)