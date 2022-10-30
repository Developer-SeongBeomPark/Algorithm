import sys
from collections import deque

T = int(sys.stdin.readline())

dx = [-2,-2,2,2,1,1,-1,-1]
dy = [-1,1,-1,1,2,-2,2,-2]

def bfs(x,y):
    q = deque([[x,y]])
    while q:
        value = q.popleft()
        a,b = value[0],value[1]
        if(value == end):
            return arr[a][b]
        if(0 <= a < N and 0 <= b < N and visited[a][b] == 0):
            visited[a][b] = 1
            for i in range(8):
                c,r = a+dx[i],b+dy[i]
                if(0 <= c < N and 0 <= r < N and visited[c][r] == 0):
                    q.append([c,r])
                    arr[c][r] = arr[a][b] + 1

answer = []

for _ in range(T):
    N = int(sys.stdin.readline())

    start = list(map(int,sys.stdin.readline().split()))

    end = list(map(int,sys.stdin.readline().split()))

    arr = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    answer.append(bfs(start[0],start[1]))

for i in answer:
    print(i)