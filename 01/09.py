import random

# get index which will be swapped
def get_idx(X):
    swap_idx = []
    for i in range(len(X)):
        #print(i)
        if len(X[i]) > 4:
            swap_idx.append(i)
    return swap_idx

x = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
x_ = x.split(' ')

idx = get_idx(x_)
tmp = idx

# shuffle index
idx = random.sample(idx, len(idx))
#print(idx)
#print(tmp)

# swap words
for (i, j) in zip(idx, tmp):
    #print(i)
    #print(j)
    x_[i], x_[j] = x_[j], x_[i]

#print(x_)
ans = ""

for i in x_:
    ans += i + ' '
    
print(x)
print(ans)


