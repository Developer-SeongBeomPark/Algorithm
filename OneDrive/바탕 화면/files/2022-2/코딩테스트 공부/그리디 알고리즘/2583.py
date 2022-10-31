import sys
sys.setrecursionlimit(10**6)

M,N,K = map(int,sys.stdin.readline().split())

area = [[0] * N for _ in range(M)]
visited = [[0] * N for _ in range(M)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

for _ in range(K):
    x_1,y_1,x_2,y_2 = map(int,sys.stdin.readline().split())
    for i in range(x_1,x_2):
        for j in range(y_1,y_2):
            area[j][i] = 1

def bfs(x,y):
    if (0 <= x < M and 0 <= y < N and visited[x][y] == 0 and area[x][y] == 0):
        visited[x][y] = 1
        global cnt
        cnt += 1
        for i in range(4):
            bfs(x+dx[i],y+dy[i])

        return 1
    else:
        return 0


total = 0
answer = []

for i in range(M):
    for j in range(N):
        cnt = 0
        if(bfs(i,j) == 1):
            total += 1
        if(cnt != 0):
            answer.append(cnt)

answer.sort()
print(total)
print(" ".join(map(str,answer)))