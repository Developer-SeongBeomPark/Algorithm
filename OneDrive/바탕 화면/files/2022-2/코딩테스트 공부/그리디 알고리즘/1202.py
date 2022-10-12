N,K = map(int,input().split())


stat = []
bag = []

for i in range(N):
    stat.append(list(map(int,input().split())))

for i in range(K):
    bag.append(int(input()))
    
stat.sort(key = lambda x : (x[0],-x[1]))
bag.sort()

total = 0

for i in bag:
    pop_value = stat.pop(0)

    if(i >= pop_value[0]):
        price = pop_value[1]
        total += price

print(total)
    