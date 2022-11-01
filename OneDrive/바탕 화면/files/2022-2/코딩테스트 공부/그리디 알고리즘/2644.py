import sys

M,N = map(int,sys.stdin.readline().split())

box = list(list(map(int,sys.stdin.readline().split())) for _ in range(N))
visited = [[0] * M for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

total = 0
cnt = 0
answer = []

def bfs(x,y):
    if(0 <= x < N and 0 <= y < M and visited[x][y] == 0):
        visited[x][y] = 1
        global cnt
        cnt += 1
        for i in range(4):
            bfs(x+dx[i],y+dy[i])
        return 1


for i in range(N):
    for j in range(M):
        cnt = 0
        if bfs(i,j) == 1:
            total += 1
        if(cnt > 0):
            answer.append(cnt)

if(total > 1):
    print(-1)
else:
    print()