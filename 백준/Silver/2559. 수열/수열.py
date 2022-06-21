import sys
input = sys.stdin.readline

n, m = map(int,input().split())

arr = list(map(int,input().split()))

new = []
temp = sum(arr[:m])
new.append(temp)

for i in range(m, n):
    temp += arr[i] - arr[i - m]
    new.append(temp)

print(max(new))
