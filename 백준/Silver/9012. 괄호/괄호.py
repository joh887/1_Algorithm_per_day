n = int(input())

for i in range(n):
    arr = []
    flag = True
    p = input()
    for j in p:
        if(j == '('):
            arr.append(j)
        if(j == ')'):
            if (len(arr) == 0):
                print('NO')
                flag = False
                break
            elif arr[-1] == '(':
                arr.pop()
            else:
                print('NO')
                break
    if(len(arr) == 0):
        if(flag == True):
            print('YES')
    else:
        print('NO')
