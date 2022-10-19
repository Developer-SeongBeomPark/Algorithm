import sys

N,K = map(int,sys.stdin.readline().split())

use_order = list(map(int,sys.stdin.readline().split()))

plug = []
num = 0

for i in range(N):
    plug.append(use_order.pop(0))

use_order_copy = use_order


    
