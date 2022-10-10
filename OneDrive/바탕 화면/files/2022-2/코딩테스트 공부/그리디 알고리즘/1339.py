N = int(input())

list = []

for i in range(N):
    list.append(input())

list.sort(key = lambda x : len(x), reverse=True)

num_list = [9,8,7,6,5,4,3,2,1]
alpha_list = []


for i in range(N):
    for j in range(len(list[i])):
        alpha = list[i][j]
        if(alpha not in alpha_list):
            alpha_list.append(alpha)
