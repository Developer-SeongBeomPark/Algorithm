from collections import defaultdict

N = int(input())

list = []

for i in range(N):
    list.append(input())

list.sort(key = lambda x : len(x), reverse=True)

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_dict = defaultdict(int)

for i in range(N):
    for j in range(len(list[i])):
        alpha_dict[list[i][j]] += 10**(len(list[i])-j-1)

value_list = alpha_dict.values()

answer_list = []
for i in value_list:
    answer_list.append(i)

answer_list.sort(reverse=True)

answer = 0

for i in range(9,9-len(answer_list),-1):
    answer += i * answer_list[9-i]

print(answer)