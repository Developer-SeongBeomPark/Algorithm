import sys
import copy
from collections import deque

N,M = map(int,sys.stdin.readline().split())

matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

answer = 0

def makewall(cnt):
    if(cnt == 3):
        global answer
        answer = max(answer,bfs())
        return

    for i in range(N):
        for j in range(M):
            if(matrix[i][j] == 0):
                matrix[i][j] = 1
                makewall(cnt + 1)
                matrix[i][j] = 0

def bfs():
    q = deque()
    matrix_copy = copy.deepcopy(matrix)
    for i in range(N):
        for j in range(M):
            if(matrix[i][j] == 2):
                q.append([i,j])

    while q:
        [x,y] = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(0 <= nx < N and 0 <= ny < M and matrix_copy[nx][ny] == 0):
                matrix_copy[nx][ny] = 2
                q.append([nx,ny])
                
    count = 0
    for i in range(N):
        for j in range(M):
            if(matrix_copy[i][j] == 0):
                count += 1

    return count
            

makewall(0)
print(answer)

