import sys
from collections import deque

def bfs(start):
    q = deque([start])
    while q:
        start = q.popleft()
        if(start == K):
            return second_count[start]
        for i in (start-1,start+1,start*2):
            if(0 <= i < 100001 and not second_count[i]):
                second_count[i] = second_count[start] + 1
                q.append(i)

N,K = map(int, sys.stdin.readline().split())

second_count = [0] * 100001

print(bfs(N))
