n = input().upper()
word_list = list(set(n))
cnt_list = []

for i in word_list:
    count = n.count(i)
    cnt_list.append(count)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")

else:
    print(word_list[(cnt_list.index(max(cnt_list)))])