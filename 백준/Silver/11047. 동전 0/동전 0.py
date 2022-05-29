N_K = list(map(int, input().split()))
N = N_K[0]
K = N_K[1]
coins= []
for i in range(N): 
    coin = int(input())
    coins.append(coin)
count = 0
for i in reversed(range(N)):
    count += K // coins[i]
    K = K % coins[i]
print(count)
