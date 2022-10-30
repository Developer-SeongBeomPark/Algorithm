import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

node = [[] for _ in range(N+1)]
visited = [0] * (N+1)
answer_node = [0] * (N+1)

for i in range(N-1):
    x,y = map(int,sys.stdin.readline().split())
    node[x].append(y)
    node[y].append(x)

def bfs(start):
    if(visited[start] == 0):
        visited[start] = 1
        for i in node[start]:
            if(visited[i] == 1):
                continue
            answer_node[i] = start
            bfs(i)

bfs(1)

for i in range(2,N+1):
    print(answer_node[i])