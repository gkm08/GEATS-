#f = open("nemfile.txt", "w")
#f.close()

#f = open("newfile.txt", "w")
#for i in range(1, 11):
 #   data = "This is line %d.\n" % i
  #  f.write(data)
#f.close()

#f = open("newfile.txt", "r")
#while True:
 #   line = f.readline()
  #  if not line: break
   # print(line)
#f.close()

#f = open("newfile.txt", "r")
#lines = f.readline() # list
#for line in lines:
 #   print(line)
#f.close()

#f = open("newfile.txt", "r")
#data = f.read() # string
#print(data)
#f.closse()

#f = open("newfile.txt", "a")
#for i in range(11, 21):
#    data = "this is line %d.\n" % i
#    f.write(data)
#f.close()

#planets = []
#f = open("planets.txt", "r")
#for line in f:
#    planets.append(line.strip())
#f.close()
#print(planets)

#f = open("planets.txt", "r")
#for line in f:
#    planets = f.readlines()
#f.close()
#print(planets)

f = open("planets.txt", "r")
current = 0
earth = 0
for line in f:
    current += 1
    planet = line.strip().lower()
    if planet == "earth":
        earth = current
print("Earth is planet #%d" % earth)
f.close()

