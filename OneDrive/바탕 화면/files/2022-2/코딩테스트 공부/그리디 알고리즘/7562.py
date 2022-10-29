import sys
from collections import deque

N = int(sys.stdin.readline())

start = list(map(int,sys.stdin.readline().split()))

end = list(map(int,sys.stdin.readline().split()))

arr = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dx = [-2,-2,2,2,1,1,-1,-1]
dy = [-1,1,-1,1,2,-2,2,-2]

def bfs(x,y):
    q = deque([x,y])
    while q:
        value = q.popleft()
        a,b = value[0],value[1]
        if(value == end):
            return arr[a][b]
        if(0 <= a < N and 0 <= b < N and visited[a][b] == 0):
            visited[a][b] = 1
            for i in range(8):
                if(0 <= a + dx[i] < N and 0 <= b + dy[i] < N and visited[a+dx[i]][b+dy[i]] == 0):
                    q.append([a+dx[i],b+dy[i]])
                    arr[a+dx[i]][b+dy[i]] = arr[a][b] + 1


print(bfs(start[0],start[1]))
