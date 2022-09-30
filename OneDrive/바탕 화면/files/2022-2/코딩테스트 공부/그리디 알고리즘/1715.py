N = int(input())

arr = []

for i in range(N):
    card = int(input())
    arr.append(card)

if(N == 1):
    print(arr[0])
    exit()
elif(N == 2):
    print(arr[0] + arr[1])
    exit()
else:
    arr.sort()

    min_count = arr[0] * (N-1)

    for i in range(1,N):
        min_count += arr[i] * (N-i)

    print(min_count)