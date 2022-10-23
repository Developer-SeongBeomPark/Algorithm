import sys

N,M = map(int, sys.stdin.readline().split())
count = 0

if(N == 1):
    count = 1
elif(N == 2):
    if(M == 1 or M == 2):
        count = 1
    elif(M == 3 or M == 4):
        count = 2
    elif(M == 5 or M == 6):
        count = 3
    else:
        count = 4
else:
    if(M <= 4):
        count = M
    elif(M == 5):
        count = M - 1
    else:
        count = M - 2

print(count)
