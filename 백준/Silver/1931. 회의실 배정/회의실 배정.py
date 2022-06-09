n = int(input())

arr = []
for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])
arr.sort(key = lambda x: (x[1],x[0]))
compare = arr[0][1]
count = 1
if(n == 1):
    print(1)
else:

    for i in range(1,len(arr)):
        if(compare <= arr[i][0]):
            count += 1
            compare = arr[i][1]
    print(count)
    
