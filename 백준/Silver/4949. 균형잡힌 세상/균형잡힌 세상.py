s = input()
while(s != '.'):
    arr = []
    flag = True
    for i in s:
        if i == '(':
            arr.append(i)
        elif i ==')':
            if len(arr) == 0:
                print('no')
                flag = False
                break
            elif arr[-1] == '(':
                arr.pop()
            else:
                print('no')
                flag = False
                break
        elif i =='[':
            arr.append(i)
        elif i ==']':
            if len(arr) == 0:
                print('no')
                flag = False
                break
            elif arr[-1] == '[':
                arr.pop()
            else:
                print('no')
                flag = False
                break
    if len(arr) == 0 and flag == True:
        print('yes')
    elif len(arr) != 0 and flag == True:
        print('no')


    s = input()