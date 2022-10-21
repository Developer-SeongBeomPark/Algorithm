import sys

N,L = map(int,sys.stdin.readline().split())

pipe = list(map(int,sys.stdin.readline().split()))

pipe.sort()

total = 1
start = pipe[0]

for i in range(1,N):
    if(pipe[i] > start + L-1):
        start = pipe[i]
        total += 1

print(total)