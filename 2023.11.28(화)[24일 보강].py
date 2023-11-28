T = int(input())

for i in range(T):
    C = int(input())
    '''
    print(C//25)
    print(C%25//10)
    print(C%25%10//5)
    print(C%25%10%5)
    '''

    for n in [25, 10, 5, 1]:
        print(C//n, end = ' ')
        C %= n