N, B = input().split()
N = N[::-1]
n = len(N)
B = int(B)

sum = 0
number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    sum+=number.index(N[i])*(B**i)

print(sum)