import sys
import heapq

N = int(sys.stdin.readline())

lecture = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

tmp = []

num = 0

heapq.heapify(lecture)
heapq.heapify(tmp)

while lecture or tmp:
    if(not tmp):
        num += 1
        [start,end] = heapq.heappop(lecture)
        for i in range(len(lecture)):
            value = heapq.heappop(lecture)
            if(value[0] >= end):
                start = value[0]
                end = value[1]
            else:
                heapq.heappush(tmp,value)

    elif(not lecture):
        num += 1
        [start,end] = heapq.heappop(tmp)
        for i in range(len(tmp)):
            value = heapq.heappop(tmp)
            if(value[0] >= end):
                start = value[0]
                end = value[1]
            else:
                heapq.heappush(tmp,value)

print(num)

## 시간 초과