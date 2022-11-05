
def gen_ngram(X, n):

    ans = []
    for i in range(len(X)-n+1):
        ans.append(X[i:i+n])
    return ans



seq = 'I am an NLPer'
seq_ = seq.split()

print(gen_ngram(seq, 2))

print(gen_ngram(seq_, 2))


