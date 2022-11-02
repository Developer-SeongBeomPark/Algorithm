import sys
from collections import deque

M,N = map(int,sys.stdin.readline().split())

box = list(list(map(int,sys.stdin.readline().split())) for _ in range(N))
dx = [-1,0,1,0]
dy = [0,-1,0,1]

q = deque([])
answer = 0
initial = True

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append([i,j])
        if box[i][j] == 0:
            initial = False

if(initial == True):
    print(0)
    exit()

def bfs():
    while q:
        [x,y] = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = x + dy[i]
            if(0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0):
                box[nx][ny] = box[x][y] + 1
                q.append([nx,ny])

bfs()

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            print(box)
            exit()
        if(box[i][j] > answer):
            answer = box[i][j]


print(answer)        