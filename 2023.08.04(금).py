#아스키 코드
#n = input()

#print(ord(n))

#숫자의 합
#len = int(input())
#n = input()
#sum = 0
#for i in n:
#    sum += int(i)

#print(sum)

#알파벳 찾기

#s = list(input())
#c = 'abcdefghijklmnopqrstuvwxxyz'

#for i in c:
#    if i in s:
#        print(s.index(i), end = ' ')
#    else:
#        print(-1, end = ' ')

#문자열 반복

t = int(input())
for _ in range(t):
    n, s = input().split()
    for i in s:
        print(i*int(n), end='')
    print()

