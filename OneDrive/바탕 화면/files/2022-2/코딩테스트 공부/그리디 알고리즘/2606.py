import sys

N = int(sys.stdin.readline())

K = int(sys.stdin.readline())

com = [[] for _ in range(N+1)]

for _ in range(K):
    a, b = map(int, sys.stdin.readline().split())
    com[a].append(b)
    com[b].append(a)

visited = [0] * (N+1)
cnt = 0

def dfs(a):
    global cnt
    visited[a] = 1
    for i in com[a]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


dfs(1)
print(cnt)