peopleNum = int(input())
num_list = list(map(int, input().split()))


num_list.sort()
total_time = 0
for i in range(len(num_list)):
    for j in range(i + 1):
        total_time += num_list[j]
print(total_time)