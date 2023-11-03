#a = ["M",11,1,4,1,[1,"print",3]]
#a+=a
#print(a)
total = int(input())
t = int(input())
sum = 0
for i in range(t):
    m, n = map(int, input().split())
    sum += m*n

if sum == total:
    print("yes")
else:
    print("no")