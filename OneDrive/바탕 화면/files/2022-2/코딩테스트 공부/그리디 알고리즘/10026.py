import sys
import copy
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

area = list(list(sys.stdin.readline().rstrip()) for _ in range(N))
area_copy = copy.deepcopy(area)
visited = [[0] * N for _ in range(N)]

dx,dy = [-1,0,1,0],[0,1,0,-1]

for i in range(N):
    for j in range(N):
        if area_copy[i][j] == "G":
            area_copy[i][j] = "R"

def bfs_R(x,y,a):
    if(0 <= x < N and 0 <= y < N 
    and visited[x][y] == 0 and a[x][y] == "R"):
        visited[x][y] = 1
        for i in range(4):
            bfs_R(x+dx[i],y+dy[i],a)
        return 1
    else:
        return 0

def bfs_G(x,y,a):
    if(0 <= x < N and 0 <= y < N 
    and visited[x][y] == 0 and a[x][y] == "G"):
        visited[x][y] = 1
        for i in range(4):
            bfs_G(x+dx[i],y+dy[i],a)
        return 1
    else:
        return 0

def bfs_B(x,y,a):
    if(0 <= x < N and 0 <= y < N 
    and visited[x][y] == 0 and a[x][y] == "B"):
        visited[x][y] = 1
        for i in range(4):
            bfs_B(x+dx[i],y+dy[i],a)
        return 1
    else:
        return 0

answer_1 = 0
answer_2 = 0

for i in range(N):
    for j in range(N):
        if(area[i][j] == "R"):
            value = bfs_R(i,j,area)
            answer_1 += value
        elif(area[i][j] == "G"):
            value = bfs_G(i,j,area)
            answer_1 += value
        elif(area[i][j] == "B"):
            value = bfs_B(i,j,area)
            answer_1 += value

visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if(area_copy[i][j] == "R"):
            value = bfs_R(i,j,area_copy)
            answer_2 += value
        elif(area_copy[i][j] == "B"):
            value = bfs_B(i,j,area_copy)
            answer_2 += value
        
print(answer_1,answer_2)

