N = int(input())


for _ in range(N):
    dic = {}
    sum = 1
    n = int(input())
    for _ in range(n):
        item, typ = input().split()


        if typ in dic:
            dic[typ] += 1
        else:
            dic[typ] = 1
    for i in dic:
        sum *= dic[i] + 1
    print(sum - 1)