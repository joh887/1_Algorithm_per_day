def tower(n, start, end, mid):
    if n == 1:
        print(start, end)
        return
    tower(n-1,start,mid,end)
    print(start,end)
    tower(n-1,mid,end,start)

n = int(input())
print(2**n -1)
tower(n,1,3,2)