N = int(input())
zero = [1,0,1]
one = [0,1,1]

def fibonacci(n):
    num = len(zero)
    if n >= num:
        for i in range(num, n + 1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
             
    print("{} {}".format(zero[n], one[n]))



for _ in range(N):
    n = int(input())
    fibonacci(n)
