s = input()

count = 0

arr = set()

for i in range(len(s)):
    for j in range(i,len(s)):
        temp = s[i:j +1]
        arr.add(temp)

print(len(arr))



