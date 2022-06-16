num = int(input())

road = list(map(int,input().split()))
city = list(map(int,input().split()))

min = city[0]
move = 0

for i in range(num - 1):
    if(min > city[i]):
        min = city[i]
    move += min * road[i]
print(move)