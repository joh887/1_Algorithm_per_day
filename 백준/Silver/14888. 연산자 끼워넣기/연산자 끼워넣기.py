ans = []

N = int(input())

num = list(map(int,input().split()))

operator = list(map(int,input().split()))



tot = num[0]




max_v = -1e9
min_v = 1e9


def getAns(idx,tot):
    global max_v, min_v
    if idx == N:
        max_v = max(max_v,tot)
        min_v = min(min_v,tot)
        return
    else:
        for op in range(len(operator)):
            if operator[op] != 0:
                if op == 0:
                    operator[op] -= 1
                    getAns(idx + 1, tot + num[idx])
                    operator[op] += 1
                elif op == 1:
                    operator[op] -= 1
                    getAns(idx + 1, tot - num[idx])
                    operator[op] += 1
                elif op == 2:
                    operator[op] -= 1
                    getAns(idx + 1, tot * num[idx])
                    operator[op] += 1
                elif op == 3:
                    operator[op] -= 1
                    if tot >= 0:
                        temp = tot // num[idx]
                    else:
                        temp = (-tot // num[idx]) * -1
                    getAns(idx + 1, temp)
                    operator[op] += 1
                    

getAns(1,num[0])
print(max_v)
print(min_v)