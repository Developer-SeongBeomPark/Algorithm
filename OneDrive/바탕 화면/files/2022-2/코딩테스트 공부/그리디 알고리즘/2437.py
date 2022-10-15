import sys


N = int(sys.stdin.readline())

weights = list(map(int,sys.stdin.readline().split()))

#처음부터 추 무게를 더해가며 자신의 앞에 있는 추 무게의 합보다 자신의 무게가 크면 그 사이값들은 표현할 수가 없음

value = 0

weights.sort()

for i in range(1,N):
    value += weights[i-1]
    if(weights[i] > value):
        value += 1
        break

print(value)

