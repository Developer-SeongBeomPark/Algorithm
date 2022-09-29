x = input().split("-")

for i in range(len(x)):
    x[i] = x[i].split("+")

total = 0

for i in range(len(x[0])):
    total += int(x[0][i])

for i in range(1, len(x)):
    value = 0
    for j in range(len(x[i])):
        value += int(x[i][j])
    total -= value

print(total)