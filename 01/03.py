from collections import Counter

a = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
a = a.split(' ')
ans = []

for i in a:
    #remove ','
    if ',' in i:
        print(i)
        i = i[:len(i)-1]
    #remove '.'
    if '.' in i:
        print(i)
        i = i[:len(i)-1]

    ans.append(len(i))

print(ans)