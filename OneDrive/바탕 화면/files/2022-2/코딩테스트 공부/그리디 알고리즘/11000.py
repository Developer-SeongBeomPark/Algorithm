import sys
import heapq

N = int(sys.stdin.readline())

lecture = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

tmp = []

lecture.sort()

###########################################
heapq.heapify(tmp)
[start,end] = lecture[0]
heapq.heappush(tmp,end)

for i in range(1,N):
    if(lecture[i][0] >= tmp[0]):
        heapq.heappop(tmp)
        heapq.heappush(tmp,lecture[i][1])
    else:
        heapq.heappush(tmp,lecture[i][1])


print(len(tmp))






