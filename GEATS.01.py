N, B = input().split()
N = int(N)
B = int(B)
s = ""
number = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while N:
    s += str(number[N%B])
    N//=B

print(s[::-1])