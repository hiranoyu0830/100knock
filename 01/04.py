from collections import defaultdict

a = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
a = a.split(' ')
ans = defaultdict(int)

for i in a:
    #remove '.'
    if '.' in i:
        #print(i)
        i = i[:len(i)-1]

for j in range(len(a)):
    if j+1 == 1 or 5 <= j+1 <= 9 or j+1 == 15 or j+1 == 16 or j+1 == 19:
        ans[a[j][0]] = j
    else:
        ans[a[j][0:2]] = j
        
print(ans)
