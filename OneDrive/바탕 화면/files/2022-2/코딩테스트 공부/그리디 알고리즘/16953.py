import sys

A,B = map(int,sys.stdin.readline().split())

def first(x):
    return int(x/2)

def second(x):
    value = str(x)
    value = value[:-1]
    if(value == ""):
        return 0
    return int(value)

count = 0

while True:
    if(B == A):
        count += 1
        break
    elif(B < A):
        count = -1
        break

    if(B % 2 == 0):
        B = first(B)
    elif(str(B)[-1] == "1"):
        B = second(B)
    else:
        count = -1
        break
    count += 1

print(count)

