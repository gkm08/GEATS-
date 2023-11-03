#새싹
#print("         ,r\'\"7")
#print("r`-_   ,\'  ,/")
#print(" \. \". L_r\'")
#print("   `~\/")
#print("      |")
#print("      |")

#크로아티아 알파벳
#croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#n = input()

#for i in croatia:
#    n = n.replace(i, 'a')
#print(len(n))

#그룹 단어 체커
n = int(input())
group_word = n
for i in range(n):
    word = input()
    for j in range(0, len(word)-1):
       if word[j] == word[j+1]:
           pass
       elif word[j] in word[j+1:]:
           group_word -= 1
           break
print(group_word)