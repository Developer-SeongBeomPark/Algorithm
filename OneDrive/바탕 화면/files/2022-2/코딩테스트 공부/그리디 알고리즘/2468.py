import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y,height):
    if(0 <= x < N and 0 <= y < N and visited[x][y] == 0):
        visited[x][y] = 1
        if(arr[x][y] > height):
            for i in range(4):
                bfs(x+dx[i],y+dy[i],height)
            return 1
    else:
        return 0


count_list = [0] * 101

for h in range(1,101):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if(bfs(i,j,h) == 1):
                cnt += 1
    count_list[h] = cnt

if(sum(count_list) == 0):
    print(1)
else:
    print(max(count_list))