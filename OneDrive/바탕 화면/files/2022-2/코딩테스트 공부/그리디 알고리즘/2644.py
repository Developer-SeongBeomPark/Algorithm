import sys

M,N = map(int,sys.stdin.readline().split())

box = list(list(map(int,sys.stdin.readline().split())) for _ in range(N))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

total = 0
cnt = 0
answer = []

def bfs(x,y):
    if(0 <= x < N and 0 <= y < M):
        if(box[x][y] == 0):
            box[x][y] = 1
            cnt += 1



for i in range(N):
    for j in range(M):
        if(box[i][j] == 1):
            for k in range(4):
                bfs(i+dx[k],j+dy[k])

print(answer)