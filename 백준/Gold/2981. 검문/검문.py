N = int(input())

num = []
new = []

for _ in range(N):
    num.append(int(input()))

num.sort()

for i in range(1,len(num)):
    new.append(num[i] - num[i-1])

def getGCD(a,b):
    if (b == 0):
        return a
    else:
        return getGCD(b, a % b)

GCD = new[0]
for idx in range(1, len(new)):
    GCD = getGCD (GCD, new[idx])


ans = []

for i in range(2, int(GCD ** 0.5) + 1):
    if (GCD % i == 0):
        ans.append(i)
        ans.append(GCD // i)
ans.append(GCD)
ans = sorted(list(set(ans)))


for i in ans:
    print(i , end = " ")




