# # O(N) = n**2 인 경우

# max_length = int(input())

# array = []

# for i in range(max_length):
#     value = input()
#     arr = list(map(int, value.split(" ")))
#     array.append(arr)

# start = array[0][0]
# end = array[0][1]
# count = 1
# max_count = 1

# for i in range(max_length - 1):
#     for j in range(i+1,max_length):

#         if(array[j][0] >= end):
#             start = array[j][0]
#             end = array[j][1]
#             count += 1
        
#     if(count > max_count):
#         max_count = count
#         count = 1

# print(max_count) # --> 시간 초과


# O(N) =  N인 경우

max_length = int(input())

array = []

for i in range(max_length):
    value = input()
    arr = list(map(int, value.split(" ")))
    array.append(arr)

array.sort(key = lambda x : (x[1],x[0])) # sort,sorted 함수의 시간 복잡도 : O(nlogn)

start = array[0][0]
end = array[0][1]
count = 1

for i in range(1,max_length):
    if(array[i][0] >= end):
        start = array[i][0]
        end = array[i][1]
        count += 1

print(count)

############################################
# array라는 배열을 각 원소배열들의 두번째 값을 기준으로 먼저 정렬하고 첫번째 값을 기준으로 재정렬하는 이유 :
# 빨리 끝나면서 빨리 시작하는 회의 순으로 정렬을 하기 때문에 


