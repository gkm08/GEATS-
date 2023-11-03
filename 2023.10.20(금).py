#10798 세로읽기
#table = [list(input()) for l in range(5)]

#for col in range(15):
#    for row in range(5):
#        if(col<len(table[row])):
#           print(table[row][col], end = '')

#2563 색종이

table = [[0 for i in range(100)] for j in range(100)]
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    for row in range(x, x+10):
        for col in range(y, y+10):
            table[row][col] = 1

result=0
for i in table:
    result += i.count(1)

print(result)