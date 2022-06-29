n,m = map(int, input().split())

arr = set()
arr2 = set()

arr= set(list(map(int, input().split())))
arr2 = set(list(map(int, input().split())))

new = (arr - arr2)
new2 = (arr2 - arr)
print(len(new) + len(new2))