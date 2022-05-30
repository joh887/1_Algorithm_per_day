n = int(input())

def gbs(a,b):
    if (b == 0):
        return a
    else:
        return (gbs(b, a % b))

for _ in range(n):
    a,b = map(int,input().split())
    s = gbs(a,b)
    print(a *b // s)
