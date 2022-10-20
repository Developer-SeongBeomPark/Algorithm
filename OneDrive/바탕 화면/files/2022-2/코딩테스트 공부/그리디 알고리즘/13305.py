import sys
from xmlrpc.client import MAXINT

N = int(sys.stdin.readline())

distance = list(map(int,sys.stdin.readline().split()))

price_list = list(map(int,sys.stdin.readline().split()))
price_list.pop()


min_price = price_list[0]
dis = distance[0]
total_price = min_price * dis

# while price_list:
#     min_price = min(price_list)
#     min_price_index = price_list.index(min_price)
#     part_sum = min_price * sum(distance[min_price_index:])
#     total_price += part_sum
#     distance = distance[:min_price_index]
#     price_list = price_list[:min_price_index]

for i in range(1, len(distance)):
    if(price_list[i] < min_price):
        min_price = price_list[i]
        
    total_price += min_price * distance[i]

print(total_price)