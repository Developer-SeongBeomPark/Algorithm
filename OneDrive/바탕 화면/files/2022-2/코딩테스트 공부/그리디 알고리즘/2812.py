import sys

N,K = map(int,sys.stdin.readline().split())

number = list(sys.stdin.readline().rstrip())

count = 0

while count < K:
    for i in range(len(number)):
        if(i == len(number) - 1):
            number.pop(i)
            count += 1
        else:
            if (number[i] < number[i+1]):
                number.pop(i)
                count += 1
                break

print("".join(number))