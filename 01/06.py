
def gen_bigram(X):

    bigram = []
    for i in range(len(X)-1):
        bigram.append(X[i:i+2])

    return bigram

a = 'paraparaparadise'
b = 'paragraph'

X = set(gen_bigram(a))
Y = set(gen_bigram(b))

wa = X.union(Y)
seki = X.intersection(Y)
sa = X.difference(Y)

print(X)
print(Y)
print(wa)
print(seki)
print(sa)

if 'se' in X:
    print('se is exist in X')
if 'se' in Y:
    print('se is exist in Y')