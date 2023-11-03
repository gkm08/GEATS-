#now = [1, 1, 2, 2, 2, 8]

#a = list(map(int,input().split()))

#for i in range(6):
#    print(now[i] - a[i], end = ' ')



#n = int(input())
#for i in range(1, n+1):
#    for h in range(n-i):
#        print(" ", end='')
#    for v in range(2*i-1):
#        print("*", end='')
#    print()


#for i in range(n-1, 0, -1):
#    for h in range(n-i):
#        print(" ", end='')
#    for v in range(2*i-1):
#        print("*", end='')
#    print()

class whatisyourmajor(object):
  def __init__(self, name, school, major):
    self.name = name()
    self.school = school()
    self.major = major()


steve = whatisyourmajor('steve', 'abs', 'computer')

