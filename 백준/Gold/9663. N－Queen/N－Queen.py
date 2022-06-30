n=int(input())

def dfs2(lv,sh0,shl,shr):
    h = 0
    shl=(shl<<1) & ((1<<n)-1)
    shr=shr>>1
    sha=sh0|shl|shr
    lv+=1
    for i in range(n):
        e=(1<<i)
        if not sha&e:
            h+=1 if lv==n else dfs2(lv,sh0|e,shl|e,shr|e)
    return h

def dfs(i):
    l=1<<i
    return 1 if 1==n else dfs2(1,l,l,l)

k=2*sum([dfs(i) for i in range(n//2)])
if n&1:
    k+=dfs(n//2)
print(k)