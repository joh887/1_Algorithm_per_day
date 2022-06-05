import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

temp = set(arr)
new = list(temp)
new.sort()

dic = {new[i]:i for i in range (len(new))}

#for i in range(len(new)):
#    dic = {new[i] : i}

for a in range(n):
    print(dic[arr[a]], end = " ")

  