A = []
B = []

rows,cols = map(int,input().split())

for i in range(rows):
    r_list = list(map(int,input().split()))
    A.append(r_list)

for i in range(rows):
    r_list = list(map(int,input().split()))
    B.append(r_list)

for i in range(rows):
    for j in range(cols):
        print((A[i][j]) + (B[i][j]), end = " ")
    print()

#A = []
#B = []

#for i in range(rows):
#    list
#    A.append