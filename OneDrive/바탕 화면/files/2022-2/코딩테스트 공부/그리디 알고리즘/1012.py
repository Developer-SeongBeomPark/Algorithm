import sys
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())
dx = [-1,0,1,0]
dy = [0,-1,0,1]

answer = []

def bfs(a,b):
    if(0 <= a < N and 0 <= b < M and visited[a][b] == False):
        visited[a][b] = True
        if(field[a][b] == 1):
            for i in range(4):
                bfs(a+dx[i],b+dy[i])
            return 1
    else:
        return 0


for _ in range(T):
    cnt = 0
    M,N,K = map(int, sys.stdin.readline().split())

    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K): 
        x,y = map(int,sys.stdin.readline().split())
        field[y][x] = 1

    for i in range(N):
        for j in range(M):
            if(bfs(i,j) == 1):
                cnt += 1

    answer.append(cnt)

for value in answer:
    print(value)