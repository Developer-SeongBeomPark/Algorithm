import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

if(N <= K):
    print(0)
    exit()

arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
arr = list(set(arr))

diff = []

for i in range(1, len(arr)):
    diff.append(arr[i] - arr[i-1])

diff.sort()

for _ in range(K-1):
    diff.pop()

print(sum(diff))