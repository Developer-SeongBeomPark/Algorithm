N = int(input())
A = list(map(int,input().split(" ")))
B = list(map(int,input().split(" ")))

A.sort()
B.sort(reverse=True)

min_value = 0

for i in range(N):
    min_value += A[i] * B[i]

print(min_value)