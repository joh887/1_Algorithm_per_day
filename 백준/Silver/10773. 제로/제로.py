N = int(input())
arr = []

for i in range(N):
    n = int(input())
    if n == 0:
        del arr[-1]
    else:
        arr.append(n)
tot = 0
for i in arr:
    tot += i
print(tot)