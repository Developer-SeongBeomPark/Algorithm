import sys

N,K = map(int,sys.stdin.readline().split())

use_order = list(map(int,sys.stdin.readline().split()))

plug = []
num = 0

for i in range(N):
    plug.append(use_order.pop(0))

use_order_copy = use_order

for i in use_order:
    if i in plug:
        use_order_copy(0)
    
    else:
        for j in plug:
            if(j not in use_order_copy):
                plug.remove(j)
                plug.append(i)
                break
        



    
