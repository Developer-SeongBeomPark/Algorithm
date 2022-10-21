import sys
N = int(sys.stdin.readline())

distance = list(map(int,sys.stdin.readline().split()))

price_list = list(map(int,sys.stdin.readline().split()))
price_list.pop()


min_price = price_list[0]
dis = distance[0]
total_price = min_price * dis

for i in range(1, len(distance)):
    if(price_list[i] < min_price):
        min_price = price_list[i]
        
    total_price += min_price * distance[i]

print(total_price)